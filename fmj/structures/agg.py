#


#


#
import fmj.constants as const

#
class Agg:
    feature_types = []


class NoAgg(Agg):
    def __init__(self):
        self.feature_types = [
            const.FeatureTypes.CONTINUOUS,
            const.FeatureTypes.ORDINAL,
            const.FeatureTypes.CATEGORICAL,
        ]
