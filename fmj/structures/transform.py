#


#


#
import fmj.constants as const

#
class Transform:
    feature_types = []


class NoTransform(Transform):
    def __init__(self):
        self.feature_types = [
            const.FeatureTypes.CONTINUOUS,
            const.FeatureTypes.ORDINAL,
            const.FeatureTypes.CATEGORICAL,
        ]
