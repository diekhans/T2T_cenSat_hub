
class TrackDbRnaSeqWriter:
    def __init__(self, superTrackTmpl, trackSetTmpl):
        self.superTrackTmpl = superTrackTmpl
        self.trackSetTmpl = trackSetTmpl

    def _writeSet(self, fh, pri, spec):
        track = spec[0]
        name = spec[1] if len(spec) > 1 else track
        print(80 * "#", file=fh)
        print(self.trackSetTmpl.format(pri=pri, track=track, name=name), file=fh)

    def writeTrackDb(self, trackSpecs, fh):
        print(self.superTrackTmpl, file=fh)
        pri = 1
        for spec in trackSpecs:
            self._writeSet(fh, pri, spec)
            pri += 1
