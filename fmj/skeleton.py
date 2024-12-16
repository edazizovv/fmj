#


#


#
import fmj.constants as const
import fmj.messages as msg
import fmj.structures as struct


#
class FeaturePolicy:
    def __init__(
            self,
            feature_type : const.FeatureTypes,
            agg : struct.agg.Agg = struct.agg.NoAgg,
            transform : struct.transform.Transform = struct.transform.NoTransform,
            missing_imp : struct.missing_imp.Imputation = struct.missing_imp.NoImputation,
            outlier_fix : struct.outlier_fix.OutlierTreatment = struct.outlier_fix.NoOutlierTreatment,
    ):

        self.feature_type = feature_type

        assert feature_type in agg.feature_types
        self._agg = agg

        assert feature_type in transform.feature_types
        self.transform = transform

        assert feature_type in missing_imp.feature_types
        self.missing_imp = missing_imp

        assert feature_type in outlier_fix.feature_types
        self.outlier_fix = outlier_fix

    @property
    def bucketing(self):
        if self.feature_type == const.FeatureTypes.CONTINUOUS:
            return self._agg
        else:
            raise NotImplementedError(
                msg.BUCKETING_WRONG_CALL.format(
                    current_agg=self._agg,
                    required_agg=const.FeatureTypes.CONTINUOUS,
                )
            )

    @property
    def order(self):
        if self.feature_type == const.FeatureTypes.ORDINAL:
            return self._agg
        else:
            raise NotImplementedError(
                msg.BUCKETING_WRONG_CALL.format(
                    current_agg=self._agg,
                    required_agg=const.FeatureTypes.ORDINAL,
                )
            )

    @property
    def grouping(self):
        if self.feature_type == const.FeatureTypes.CATEGORICAL:
            return self._agg
        else:
            raise NotImplementedError(
                msg.BUCKETING_WRONG_CALL.format(
                    current_agg=self._agg,
                    required_agg=const.FeatureTypes.CATEGORICAL,
                )
            )


class ContinuousFeature(FeaturePolicy):
    def __init__(
            self,
            agg: struct.agg.Agg = struct.agg.NoAgg,
            transform: struct.transform.Transform = struct.transform.NoTransform,
            missing_imp: struct.missing_imp.Imputation = struct.missing_imp.NoImputation,
            outlier_fix: struct.outlier_fix.OutlierTreatment = struct.outlier_fix.NoOutlierTreatment,
    ):
        feature_type = const.FeatureTypes.CONTINUOUS
        super().__init__(
            feature_type=feature_type,
            agg=agg,
            transform=transform,
            missing_imp=missing_imp,
            outlier_fix=outlier_fix,
        )


class OrdinalFeature(FeaturePolicy):
    def __init__(
            self,
            agg: struct.agg.Agg = struct.agg.NoAgg,
            transform: struct.transform.Transform = struct.transform.NoTransform,
            missing_imp: struct.missing_imp.Imputation = struct.missing_imp.NoImputation,
            outlier_fix: struct.outlier_fix.OutlierTreatment = struct.outlier_fix.NoOutlierTreatment,
    ):
        feature_type = const.FeatureTypes.CONTINUOUS
        super().__init__(
            feature_type=feature_type,
            agg=agg,
            transform=transform,
            missing_imp=missing_imp,
            outlier_fix=outlier_fix,
        )


class CategoricalFeature(FeaturePolicy):
    def __init__(
            self,
            agg: struct.agg.Agg = struct.agg.NoAgg,
            transform: struct.transform.Transform = struct.transform.NoTransform,
            missing_imp: struct.missing_imp.Imputation = struct.missing_imp.NoImputation,
            outlier_fix: struct.outlier_fix.OutlierTreatment = struct.outlier_fix.NoOutlierTreatment,
    ):
        feature_type = const.FeatureTypes.CONTINUOUS
        super().__init__(
            feature_type=feature_type,
            agg=agg,
            transform=transform,
            missing_imp=missing_imp,
            outlier_fix=outlier_fix,
        )
