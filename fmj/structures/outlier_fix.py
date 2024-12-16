#


#


#
import fmj.constants as const

#
class OutlierTreatment:
    feature_types = []


class NoOutlierTreatment(OutlierTreatment):
    def __init__(self):
        self.feature_types = [
            const.FeatureTypes.CONTINUOUS,
            const.FeatureTypes.ORDINAL,
            const.FeatureTypes.CATEGORICAL,
        ]
