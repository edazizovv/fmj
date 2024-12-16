#


#


#
import fmj.constants as const

#
class Imputation:
    feature_types = []


class NoImputation(Imputation):
    def __init__(self):
        self.feature_types = [
            const.FeatureTypes.CONTINUOUS,
            const.FeatureTypes.ORDINAL,
            const.FeatureTypes.CATEGORICAL,
        ]
