import typing
from mp4_atom import MP4Atom


class MP4(dict):

    def __init__(self, file: typing.BinaryIO, store_mdat=False, *arg, **kw):
        super(MP4, self).__init__(*arg, **kw)
        self.atoms = []
        tag = None
        while tag != b'':
            size_bytes = file.read(4)
            if size_bytes == b'':
                break

            size = int.from_bytes(size_bytes, byteorder='big')
            tag = file.read(4)
            if tag == b'':
                break

            if tag == b'mdat' and not store_mdat:
                file.seek(size - 8, 1)
                continue
            atom = MP4Atom(size_bytes, tag, file.read(size - 8))
            if tag not in self:
                self[tag] = []
            self[tag].append(atom)
            self.atoms.append(atom)

    def __repr__(self):
        ret = ''
        for atom in self.atoms:
            ret += self.atom_recurse_repr(atom, '')
        return ret

    def atom_recurse_repr(self, atom, pad):
        ret = pad + str(atom) + '\n'
        for key, value in atom.items():
            for _atom in value:
                ret += self.atom_recurse_repr(_atom, pad + '    ')
        return ret

    def __setitem__(self, key, item):
        if not isinstance(key, bytes):
            key = str.encode(str(key))
        super(MP4, self).__setitem__(key, item)

    def __getitem__(self, key):
        is_string = False
        if not isinstance(key, bytes):
            is_string = True
            key = str.encode(str(key))
        value = super(MP4, self).__getitem__(key)
        if len(value) == 1 and is_string:
            return value[0]
        return value

    def __delitem__(self, key):
        if not isinstance(key, bytes):
            key = str.encode(str(key))
        super(MP4, self).__delitem__(key)
