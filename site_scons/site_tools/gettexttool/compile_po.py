# -*- coding: utf-8 -*-
import os
import struct
import io
import gettext
import re

import ast

def parse_po(filename):
    """Simple robust PO parser supporting multiline and escaped strings."""
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    catalog = {}
    msgid = None
    msgstr = None
    state = None  # 'msgid' or 'msgstr'

    def unescape(s):
        s = s.strip()
        if not (s.startswith('"') and s.endswith('"')):
            s = f'"{s}"'
        try:
            return ast.literal_eval(s)
        except Exception:
            return s.strip('"')

    for line in lines:
        line = line.strip()
        if not line or line.startswith('#'):
            continue

        if line.startswith('msgid '):
            if msgid is not None and msgstr is not None:
                catalog[msgid] = msgstr
            msgid = unescape(line[6:])
            msgstr = None
            state = 'msgid'
        elif line.startswith('msgstr '):
            msgstr = unescape(line[7:])
            state = 'msgstr'
        elif line.startswith('"'):
            part = unescape(line)
            if state == 'msgid':
                msgid += part
            elif state == 'msgstr':
                msgstr += part

    if msgid is not None and msgstr is not None:
        catalog[msgid] = msgstr

    return catalog

def compile_po_to_mo(po_path, mo_path):
    catalog = parse_po(po_path)
    # The MO format requires keys to be sorted
    keys = sorted(catalog.keys())
    num_strings = len(keys)

    # Offsets
    orig_table_offset = 28
    trans_table_offset = orig_table_offset + num_strings * 8
    strings_start = trans_table_offset + num_strings * 8

    orig_table = []
    trans_table = []
    str_data = bytearray()

    for k in keys:
        k_bytes = k.encode('utf-8') + b'\x00'
        v_bytes = catalog[k].encode('utf-8') + b'\x00'

        orig_table.append((len(k_bytes) - 1, strings_start + len(str_data)))
        str_data.extend(k_bytes)

        trans_table.append((len(v_bytes) - 1, strings_start + len(str_data)))
        str_data.extend(v_bytes)

    buf = bytearray()
    # Magic, revision, num_strings, orig_table_offset, trans_table_offset, hash_table_size, hash_table_offset
    buf.extend(struct.pack('<Iiiiiii', 0x950412de, 0, num_strings, orig_table_offset, trans_table_offset, 0, 0))
    for length, offset in orig_table:
        buf.extend(struct.pack('<ii', length, offset))
    for length, offset in trans_table:
        buf.extend(struct.pack('<ii', length, offset))
    buf.extend(str_data)

    os.makedirs(os.path.dirname(os.path.abspath(mo_path)), exist_ok=True)
    with open(mo_path, 'wb') as f:
        f.write(buf)

if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 3:
        compile_po_to_mo(sys.argv[1], sys.argv[2])
        print(f"Compiled {sys.argv[1]} -> {sys.argv[2]}")
