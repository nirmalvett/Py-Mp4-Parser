# Based on https://bitbucket.org/wez/atomicparsley/src/9183fff907bf48ce81fbf6fe5777a55120a447e2/src/AtomDefs.h
CHILD_ATOM = 0
PARENT_ATOM = 1
DUAL_ATOM = 2

ATOM_DEFINITIONS = {
    b'ftyp': CHILD_ATOM,
    b'moov': PARENT_ATOM,
    b'mvhd': CHILD_ATOM,
    b'iods': CHILD_ATOM,
    b'drm ': CHILD_ATOM,
    b'trak': PARENT_ATOM,
    b'tkhd': CHILD_ATOM,
    b'tref': PARENT_ATOM,
    b'IKEY': CHILD_ATOM,
    b'hint': CHILD_ATOM,
    b'dpnd': CHILD_ATOM,
    b'ipir': CHILD_ATOM,
    b'mpod': CHILD_ATOM,
    b'sync': CHILD_ATOM,
    b'chap': CHILD_ATOM,
    b'mdia': PARENT_ATOM,
    b'mdhd': CHILD_ATOM,
    b'minf': PARENT_ATOM,
    b'vmhd': CHILD_ATOM,
    b'smhd': CHILD_ATOM,
    b'hmhd': CHILD_ATOM,
    b'nmhd': CHILD_ATOM,
    b'gmhd': CHILD_ATOM,
    b'stbl': PARENT_ATOM,
    b'stts': CHILD_ATOM,
    b'ctts': CHILD_ATOM,
    b'stsd': DUAL_ATOM,
    b'stsz': CHILD_ATOM,
    b'sts2': CHILD_ATOM,
    b'stsc': CHILD_ATOM,
    b'stco': CHILD_ATOM,
    b'co64': CHILD_ATOM,
    b'stss': CHILD_ATOM,
    b'stsh': CHILD_ATOM,
    b'stdp': CHILD_ATOM,
    b'padb': CHILD_ATOM,
    b'stps': CHILD_ATOM,
    b'tapt': PARENT_ATOM,
    b'clef': CHILD_ATOM,
    b'prof': CHILD_ATOM,
    b'enof': CHILD_ATOM,
    b'edts': PARENT_ATOM,
    b'elst': CHILD_ATOM,
    b'mvex': PARENT_ATOM,
    b'mehd': CHILD_ATOM,
    b'trex': CHILD_ATOM,
    b'mdat': CHILD_ATOM,
    b'pdin': CHILD_ATOM,
    b'moof': PARENT_ATOM,
    b'mfhd': CHILD_ATOM,
    b'traf': PARENT_ATOM,
    b'tfhd': CHILD_ATOM,
    b'trun': CHILD_ATOM,
    b'mfra': PARENT_ATOM,
    b'tfra': CHILD_ATOM,
    b'mfro': CHILD_ATOM,
    b'free': CHILD_ATOM,
    b'skip': CHILD_ATOM,
    b'uuid': CHILD_ATOM,
    b'hdlr': CHILD_ATOM,
    b'dinf': PARENT_ATOM,
    b'dref': DUAL_ATOM,
    b'url ': CHILD_ATOM,
    b'urn ': CHILD_ATOM,
    b'alis': CHILD_ATOM,
    b'cios': CHILD_ATOM,
    b'sdtp': CHILD_ATOM,
    b'sbgp': CHILD_ATOM,
    b'udta': PARENT_ATOM,
    b'hnti': PARENT_ATOM,
    # b'rtp ': CHILD_ATOM,
    b'sdp ': CHILD_ATOM,
    b'meta': DUAL_ATOM,
    b'xml ': CHILD_ATOM,
    b'bxml': CHILD_ATOM,
    b'iloc': CHILD_ATOM,
    b'pitm': CHILD_ATOM,
    b'ipro': PARENT_ATOM,
    b'iinf': DUAL_ATOM,
    b'infe': CHILD_ATOM,
    b'subs': CHILD_ATOM,
    b'sinf': PARENT_ATOM,
    b'frma': CHILD_ATOM,
    b'imif': CHILD_ATOM,
    b'skcr': CHILD_ATOM,
    b'schm': CHILD_ATOM,
    b'schi': DUAL_ATOM,
    b'user': CHILD_ATOM,
    b'key ': CHILD_ATOM,
    b'iviv': CHILD_ATOM,
    b'righ': CHILD_ATOM,
    b'name': CHILD_ATOM,
    b'priv': CHILD_ATOM,
    b'iKMS': CHILD_ATOM,
    b'iSFM': CHILD_ATOM,
    b'iSLT': CHILD_ATOM,
    b'ipmc': CHILD_ATOM,
    b'tims': CHILD_ATOM,
    b'tsro': CHILD_ATOM,
    b'snro': CHILD_ATOM,
    b'srpp': CHILD_ATOM,
    b'hinf': PARENT_ATOM,
    b'trpy': CHILD_ATOM,
    b'nump': CHILD_ATOM,
    b'tpyl': CHILD_ATOM,
    b'totl': CHILD_ATOM,
    b'npck': CHILD_ATOM,
    b'maxr': CHILD_ATOM,
    b'dmed': CHILD_ATOM,
    b'dimm': CHILD_ATOM,
    b'drep': CHILD_ATOM,
    b'tmin': CHILD_ATOM,
    b'tmax': CHILD_ATOM,
    b'pmax': CHILD_ATOM,
    b'dmax': CHILD_ATOM,
    b'payt': CHILD_ATOM,
    b'tpay': CHILD_ATOM,
    b'drms': DUAL_ATOM,
    b'drmi': DUAL_ATOM,
    b'alac': DUAL_ATOM,
    b'mp4a': DUAL_ATOM,
    b'mp4s': DUAL_ATOM,
    b'mp4v': DUAL_ATOM,
    b'avc1': DUAL_ATOM,
    b'avcp': DUAL_ATOM,
    b'text': DUAL_ATOM,
    b'jpeg': DUAL_ATOM,
    b'tx3g': DUAL_ATOM,
    b'rtp ': DUAL_ATOM,
    b'srtp': DUAL_ATOM,
    b'enca': DUAL_ATOM,
    b'encv': DUAL_ATOM,
    b'enct': DUAL_ATOM,
    b'encs': DUAL_ATOM,
    b'samr': DUAL_ATOM,
    b'sawb': DUAL_ATOM,
    b'sawp': DUAL_ATOM,
    b's263': DUAL_ATOM,
    b'sevc': DUAL_ATOM,
    b'sqcp': DUAL_ATOM,
    b'ssmv': DUAL_ATOM,
    b'tmcd': DUAL_ATOM,
    b'mjp2': DUAL_ATOM,
    # b'alac': CHILD_ATOM,
    b'avcC': CHILD_ATOM,
    b'damr': CHILD_ATOM,
    b'd263': CHILD_ATOM,
    b'dawp': CHILD_ATOM,
    b'devc': CHILD_ATOM,
    b'dqcp': CHILD_ATOM,
    b'dsmv': CHILD_ATOM,
    b'bitr': CHILD_ATOM,
    b'btrt': CHILD_ATOM,
    b'm4ds': CHILD_ATOM,
    b'ftab': CHILD_ATOM,
    b'jp2h': PARENT_ATOM,
    b'ihdr': CHILD_ATOM,
    b'colr': CHILD_ATOM,
    b'fiel': CHILD_ATOM,
    b'jp2p': CHILD_ATOM,
    b'jsub': CHILD_ATOM,
    b'orfo': CHILD_ATOM,
    b'cprt': CHILD_ATOM,
    b'titl': CHILD_ATOM,
    b'auth': CHILD_ATOM,
    b'perf': CHILD_ATOM,
    b'gnre': CHILD_ATOM,
    b'dscp': CHILD_ATOM,
    b'albm': CHILD_ATOM,
    b'yrrc': CHILD_ATOM,
    b'rtng': CHILD_ATOM,
    b'clsf': CHILD_ATOM,
    b'kywd': CHILD_ATOM,
    b'loci': CHILD_ATOM,
    b'ID32': CHILD_ATOM,
    b'tsel': CHILD_ATOM,
    b'ilst': PARENT_ATOM,
    b'----': PARENT_ATOM,
    b'mean': CHILD_ATOM,
    b'.><.': CHILD_ATOM,
    b'esds': CHILD_ATOM,
    b'(..)': PARENT_ATOM,
    b'data': CHILD_ATOM,
}


class MP4Atom(dict):

    def __init__(self, size: bytes, name: bytes, data: bytes, *arg, **kw):
        super(MP4Atom, self).__init__(*arg, **kw)
        self.name = name
        self.size = size
        self.value = None
        if name not in ATOM_DEFINITIONS:
            self.value = data
            return
        state = ATOM_DEFINITIONS[name]
        if state == CHILD_ATOM:
            self.value = data
        elif state == PARENT_ATOM:
            pointer = 0
            while pointer < len(data):
                size_bytes = data[pointer: pointer + 4]
                size = int.from_bytes(size_bytes, byteorder='big')
                tag = data[pointer + 4: pointer + 8]
                if tag not in self:
                    self[tag] = []
                self[tag].append(MP4Atom(size_bytes, tag, data[pointer + 8: pointer + size]))
                pointer += size
        elif state == DUAL_ATOM:
            # Don't know what to do with these yet
            self.value = data

    def __repr__(self):
        return 'tag=' + str(self.name) + ' size=' + str(int.from_bytes(self.size, byteorder='big'))

    def __setitem__(self, key, item):
        if not isinstance(key, bytes):
            key = str.encode(str(key))
        super(MP4Atom, self).__setitem__(key, item)

    def __getitem__(self, key):
        is_string = False
        if not isinstance(key, bytes):
            is_string = True
            key = str.encode(str(key))
        value = super(MP4Atom, self).__getitem__(key)
        if len(value) == 1 and is_string:
            return value[0]
        return value

    def __delitem__(self, key):
        if not isinstance(key, bytes):
            key = str.encode(str(key))
        super(MP4Atom, self).__delitem__(key)

