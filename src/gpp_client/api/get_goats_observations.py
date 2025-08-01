# Generated by ariadne-codegen
# Source: src/queries

from typing import Annotated, Any, List, Literal, Optional, Union

from pydantic import Field

from .base_model import BaseModel
from .enums import (
    AttachmentType,
    Band,
    BrightnessIntegratedUnits,
    CloudExtinctionPreset,
    ExecutionState,
    GmosAmpReadMode,
    GmosBinning,
    GmosNorthBuiltinFpu,
    GmosNorthFilter,
    GmosNorthGrating,
    GmosRoi,
    GmosSouthBuiltinFpu,
    GmosSouthFilter,
    GmosSouthGrating,
    ImageQualityPreset,
    Instrument,
    ObservingModeType,
    PosAngleConstraintMode,
    ScienceBand,
    ScienceMode,
    SkyBackground,
    TimingWindowInclusion,
    WaterVapor,
)


class GetGOATSObservations(BaseModel):
    observations: "GetGOATSObservationsObservations"


class GetGOATSObservationsObservations(BaseModel):
    matches: List["GetGOATSObservationsObservationsMatches"]
    has_more: bool = Field(alias="hasMore")


class GetGOATSObservationsObservationsMatches(BaseModel):
    id: Any
    reference: Optional["GetGOATSObservationsObservationsMatchesReference"]
    instrument: Optional[Instrument]
    title: Any
    constraint_set: "GetGOATSObservationsObservationsMatchesConstraintSet" = Field(
        alias="constraintSet"
    )
    attachments: List["GetGOATSObservationsObservationsMatchesAttachments"]
    timing_windows: List["GetGOATSObservationsObservationsMatchesTimingWindows"] = (
        Field(alias="timingWindows")
    )
    target_environment: "GetGOATSObservationsObservationsMatchesTargetEnvironment" = (
        Field(alias="targetEnvironment")
    )
    pos_angle_constraint: (
        "GetGOATSObservationsObservationsMatchesPosAngleConstraint"
    ) = Field(alias="posAngleConstraint")
    science_band: Optional[ScienceBand] = Field(alias="scienceBand")
    observation_duration: Optional[
        "GetGOATSObservationsObservationsMatchesObservationDuration"
    ] = Field(alias="observationDuration")
    observer_notes: Optional[Any] = Field(alias="observerNotes")
    execution: "GetGOATSObservationsObservationsMatchesExecution"
    science_requirements: (
        "GetGOATSObservationsObservationsMatchesScienceRequirements"
    ) = Field(alias="scienceRequirements")
    observing_mode: Optional["GetGOATSObservationsObservationsMatchesObservingMode"] = (
        Field(alias="observingMode")
    )


class GetGOATSObservationsObservationsMatchesReference(BaseModel):
    label: Any


class GetGOATSObservationsObservationsMatchesConstraintSet(BaseModel):
    image_quality: ImageQualityPreset = Field(alias="imageQuality")
    cloud_extinction: CloudExtinctionPreset = Field(alias="cloudExtinction")
    sky_background: SkyBackground = Field(alias="skyBackground")
    water_vapor: WaterVapor = Field(alias="waterVapor")
    elevation_range: (
        "GetGOATSObservationsObservationsMatchesConstraintSetElevationRange"
    ) = Field(alias="elevationRange")


class GetGOATSObservationsObservationsMatchesConstraintSetElevationRange(BaseModel):
    air_mass: Optional[
        "GetGOATSObservationsObservationsMatchesConstraintSetElevationRangeAirMass"
    ] = Field(alias="airMass")
    hour_angle: Optional[
        "GetGOATSObservationsObservationsMatchesConstraintSetElevationRangeHourAngle"
    ] = Field(alias="hourAngle")


class GetGOATSObservationsObservationsMatchesConstraintSetElevationRangeAirMass(
    BaseModel
):
    min: Any
    max: Any


class GetGOATSObservationsObservationsMatchesConstraintSetElevationRangeHourAngle(
    BaseModel
):
    min_hours: Any = Field(alias="minHours")
    max_hours: Any = Field(alias="maxHours")


class GetGOATSObservationsObservationsMatchesAttachments(BaseModel):
    id: Any
    attachment_type: AttachmentType = Field(alias="attachmentType")
    file_name: Any = Field(alias="fileName")
    description: Optional[Any]
    updated_at: Any = Field(alias="updatedAt")


class GetGOATSObservationsObservationsMatchesTimingWindows(BaseModel):
    inclusion: TimingWindowInclusion
    start_utc: Any = Field(alias="startUtc")
    end: Optional[
        Annotated[
            Union[
                "GetGOATSObservationsObservationsMatchesTimingWindowsEndTimingWindowEndAt",
                "GetGOATSObservationsObservationsMatchesTimingWindowsEndTimingWindowEndAfter",
            ],
            Field(discriminator="typename__"),
        ]
    ]


class GetGOATSObservationsObservationsMatchesTimingWindowsEndTimingWindowEndAt(
    BaseModel
):
    typename__: Literal["TimingWindowEndAt"] = Field(alias="__typename")
    at_utc: Any = Field(alias="atUtc")


class GetGOATSObservationsObservationsMatchesTimingWindowsEndTimingWindowEndAfter(
    BaseModel
):
    typename__: Literal["TimingWindowEndAfter"] = Field(alias="__typename")
    after: "GetGOATSObservationsObservationsMatchesTimingWindowsEndTimingWindowEndAfterAfter"
    repeat: Optional[
        "GetGOATSObservationsObservationsMatchesTimingWindowsEndTimingWindowEndAfterRepeat"
    ]


class GetGOATSObservationsObservationsMatchesTimingWindowsEndTimingWindowEndAfterAfter(
    BaseModel
):
    seconds: Any


class GetGOATSObservationsObservationsMatchesTimingWindowsEndTimingWindowEndAfterRepeat(
    BaseModel
):
    period: "GetGOATSObservationsObservationsMatchesTimingWindowsEndTimingWindowEndAfterRepeatPeriod"
    times: Optional[Any]


class GetGOATSObservationsObservationsMatchesTimingWindowsEndTimingWindowEndAfterRepeatPeriod(
    BaseModel
):
    seconds: Any


class GetGOATSObservationsObservationsMatchesTargetEnvironment(BaseModel):
    first_science_target: Optional[
        "GetGOATSObservationsObservationsMatchesTargetEnvironmentFirstScienceTarget"
    ] = Field(alias="firstScienceTarget")


class GetGOATSObservationsObservationsMatchesTargetEnvironmentFirstScienceTarget(
    BaseModel
):
    sidereal: Optional[
        "GetGOATSObservationsObservationsMatchesTargetEnvironmentFirstScienceTargetSidereal"
    ]
    source_profile: (
        "GetGOATSObservationsObservationsMatchesTargetEnvironmentFirstScienceTargetSourceProfile"
    ) = Field(alias="sourceProfile")


class GetGOATSObservationsObservationsMatchesTargetEnvironmentFirstScienceTargetSidereal(
    BaseModel
):
    proper_motion: Optional[
        "GetGOATSObservationsObservationsMatchesTargetEnvironmentFirstScienceTargetSiderealProperMotion"
    ] = Field(alias="properMotion")
    parallax: Optional[
        "GetGOATSObservationsObservationsMatchesTargetEnvironmentFirstScienceTargetSiderealParallax"
    ]
    radial_velocity: Optional[
        "GetGOATSObservationsObservationsMatchesTargetEnvironmentFirstScienceTargetSiderealRadialVelocity"
    ] = Field(alias="radialVelocity")


class GetGOATSObservationsObservationsMatchesTargetEnvironmentFirstScienceTargetSiderealProperMotion(
    BaseModel
):
    ra: "GetGOATSObservationsObservationsMatchesTargetEnvironmentFirstScienceTargetSiderealProperMotionRa"
    dec: "GetGOATSObservationsObservationsMatchesTargetEnvironmentFirstScienceTargetSiderealProperMotionDec"


class GetGOATSObservationsObservationsMatchesTargetEnvironmentFirstScienceTargetSiderealProperMotionRa(
    BaseModel
):
    milliarcseconds_per_year: Any = Field(alias="milliarcsecondsPerYear")


class GetGOATSObservationsObservationsMatchesTargetEnvironmentFirstScienceTargetSiderealProperMotionDec(
    BaseModel
):
    milliarcseconds_per_year: Any = Field(alias="milliarcsecondsPerYear")


class GetGOATSObservationsObservationsMatchesTargetEnvironmentFirstScienceTargetSiderealParallax(
    BaseModel
):
    milliarcseconds: Any


class GetGOATSObservationsObservationsMatchesTargetEnvironmentFirstScienceTargetSiderealRadialVelocity(
    BaseModel
):
    kilometers_per_second: Any = Field(alias="kilometersPerSecond")


class GetGOATSObservationsObservationsMatchesTargetEnvironmentFirstScienceTargetSourceProfile(
    BaseModel
):
    point: Optional[
        "GetGOATSObservationsObservationsMatchesTargetEnvironmentFirstScienceTargetSourceProfilePoint"
    ]


class GetGOATSObservationsObservationsMatchesTargetEnvironmentFirstScienceTargetSourceProfilePoint(
    BaseModel
):
    band_normalized: Optional[
        "GetGOATSObservationsObservationsMatchesTargetEnvironmentFirstScienceTargetSourceProfilePointBandNormalized"
    ] = Field(alias="bandNormalized")


class GetGOATSObservationsObservationsMatchesTargetEnvironmentFirstScienceTargetSourceProfilePointBandNormalized(
    BaseModel
):
    brightnesses: List[
        "GetGOATSObservationsObservationsMatchesTargetEnvironmentFirstScienceTargetSourceProfilePointBandNormalizedBrightnesses"
    ]


class GetGOATSObservationsObservationsMatchesTargetEnvironmentFirstScienceTargetSourceProfilePointBandNormalizedBrightnesses(
    BaseModel
):
    band: Band
    value: Any
    units: BrightnessIntegratedUnits


class GetGOATSObservationsObservationsMatchesPosAngleConstraint(BaseModel):
    mode: PosAngleConstraintMode
    angle: "GetGOATSObservationsObservationsMatchesPosAngleConstraintAngle"


class GetGOATSObservationsObservationsMatchesPosAngleConstraintAngle(BaseModel):
    degrees: Any


class GetGOATSObservationsObservationsMatchesObservationDuration(BaseModel):
    seconds: Any
    minutes: Any
    hours: Any
    iso: str


class GetGOATSObservationsObservationsMatchesExecution(BaseModel):
    execution_state: ExecutionState = Field(alias="executionState")


class GetGOATSObservationsObservationsMatchesScienceRequirements(BaseModel):
    mode: Optional[ScienceMode]
    spectroscopy: Optional[
        "GetGOATSObservationsObservationsMatchesScienceRequirementsSpectroscopy"
    ]
    exposure_time_mode: Optional[
        "GetGOATSObservationsObservationsMatchesScienceRequirementsExposureTimeMode"
    ] = Field(alias="exposureTimeMode")


class GetGOATSObservationsObservationsMatchesScienceRequirementsSpectroscopy(BaseModel):
    wavelength: Optional[
        "GetGOATSObservationsObservationsMatchesScienceRequirementsSpectroscopyWavelength"
    ]
    resolution: Optional[Any]
    wavelength_coverage: Optional[
        "GetGOATSObservationsObservationsMatchesScienceRequirementsSpectroscopyWavelengthCoverage"
    ] = Field(alias="wavelengthCoverage")


class GetGOATSObservationsObservationsMatchesScienceRequirementsSpectroscopyWavelength(
    BaseModel
):
    nanometers: Any


class GetGOATSObservationsObservationsMatchesScienceRequirementsSpectroscopyWavelengthCoverage(
    BaseModel
):
    nanometers: Any


class GetGOATSObservationsObservationsMatchesScienceRequirementsExposureTimeMode(
    BaseModel
):
    signal_to_noise: Optional[
        "GetGOATSObservationsObservationsMatchesScienceRequirementsExposureTimeModeSignalToNoise"
    ] = Field(alias="signalToNoise")
    time_and_count: Optional[
        "GetGOATSObservationsObservationsMatchesScienceRequirementsExposureTimeModeTimeAndCount"
    ] = Field(alias="timeAndCount")


class GetGOATSObservationsObservationsMatchesScienceRequirementsExposureTimeModeSignalToNoise(
    BaseModel
):
    value: Any
    at: "GetGOATSObservationsObservationsMatchesScienceRequirementsExposureTimeModeSignalToNoiseAt"


class GetGOATSObservationsObservationsMatchesScienceRequirementsExposureTimeModeSignalToNoiseAt(
    BaseModel
):
    nanometers: Any


class GetGOATSObservationsObservationsMatchesScienceRequirementsExposureTimeModeTimeAndCount(
    BaseModel
):
    time: "GetGOATSObservationsObservationsMatchesScienceRequirementsExposureTimeModeTimeAndCountTime"
    count: Any
    at: "GetGOATSObservationsObservationsMatchesScienceRequirementsExposureTimeModeTimeAndCountAt"


class GetGOATSObservationsObservationsMatchesScienceRequirementsExposureTimeModeTimeAndCountTime(
    BaseModel
):
    seconds: Any


class GetGOATSObservationsObservationsMatchesScienceRequirementsExposureTimeModeTimeAndCountAt(
    BaseModel
):
    nanometers: Any


class GetGOATSObservationsObservationsMatchesObservingMode(BaseModel):
    instrument: Instrument
    mode: ObservingModeType
    gmos_north_long_slit: Optional[
        "GetGOATSObservationsObservationsMatchesObservingModeGmosNorthLongSlit"
    ] = Field(alias="gmosNorthLongSlit")
    gmos_south_long_slit: Optional[
        "GetGOATSObservationsObservationsMatchesObservingModeGmosSouthLongSlit"
    ] = Field(alias="gmosSouthLongSlit")


class GetGOATSObservationsObservationsMatchesObservingModeGmosNorthLongSlit(BaseModel):
    grating: GmosNorthGrating
    filter: Optional[GmosNorthFilter]
    fpu: GmosNorthBuiltinFpu
    spatial_offsets: List[
        "GetGOATSObservationsObservationsMatchesObservingModeGmosNorthLongSlitSpatialOffsets"
    ] = Field(alias="spatialOffsets")
    central_wavelength: (
        "GetGOATSObservationsObservationsMatchesObservingModeGmosNorthLongSlitCentralWavelength"
    ) = Field(alias="centralWavelength")
    wavelength_dithers: List[
        "GetGOATSObservationsObservationsMatchesObservingModeGmosNorthLongSlitWavelengthDithers"
    ] = Field(alias="wavelengthDithers")
    x_bin: GmosBinning = Field(alias="xBin")
    y_bin: GmosBinning = Field(alias="yBin")
    amp_read_mode: GmosAmpReadMode = Field(alias="ampReadMode")
    roi: GmosRoi


class GetGOATSObservationsObservationsMatchesObservingModeGmosNorthLongSlitSpatialOffsets(
    BaseModel
):
    arcseconds: Any


class GetGOATSObservationsObservationsMatchesObservingModeGmosNorthLongSlitCentralWavelength(
    BaseModel
):
    nanometers: Any


class GetGOATSObservationsObservationsMatchesObservingModeGmosNorthLongSlitWavelengthDithers(
    BaseModel
):
    nanometers: Any


class GetGOATSObservationsObservationsMatchesObservingModeGmosSouthLongSlit(BaseModel):
    grating: GmosSouthGrating
    filter: Optional[GmosSouthFilter]
    fpu: GmosSouthBuiltinFpu
    spatial_offsets: List[
        "GetGOATSObservationsObservationsMatchesObservingModeGmosSouthLongSlitSpatialOffsets"
    ] = Field(alias="spatialOffsets")
    central_wavelength: (
        "GetGOATSObservationsObservationsMatchesObservingModeGmosSouthLongSlitCentralWavelength"
    ) = Field(alias="centralWavelength")
    wavelength_dithers: List[
        "GetGOATSObservationsObservationsMatchesObservingModeGmosSouthLongSlitWavelengthDithers"
    ] = Field(alias="wavelengthDithers")
    x_bin: GmosBinning = Field(alias="xBin")
    y_bin: GmosBinning = Field(alias="yBin")
    amp_read_mode: GmosAmpReadMode = Field(alias="ampReadMode")
    roi: GmosRoi


class GetGOATSObservationsObservationsMatchesObservingModeGmosSouthLongSlitSpatialOffsets(
    BaseModel
):
    arcseconds: Any


class GetGOATSObservationsObservationsMatchesObservingModeGmosSouthLongSlitCentralWavelength(
    BaseModel
):
    nanometers: Any


class GetGOATSObservationsObservationsMatchesObservingModeGmosSouthLongSlitWavelengthDithers(
    BaseModel
):
    nanometers: Any


GetGOATSObservations.model_rebuild()
GetGOATSObservationsObservations.model_rebuild()
GetGOATSObservationsObservationsMatches.model_rebuild()
GetGOATSObservationsObservationsMatchesConstraintSet.model_rebuild()
GetGOATSObservationsObservationsMatchesConstraintSetElevationRange.model_rebuild()
GetGOATSObservationsObservationsMatchesTimingWindows.model_rebuild()
GetGOATSObservationsObservationsMatchesTimingWindowsEndTimingWindowEndAfter.model_rebuild()
GetGOATSObservationsObservationsMatchesTimingWindowsEndTimingWindowEndAfterRepeat.model_rebuild()
GetGOATSObservationsObservationsMatchesTargetEnvironment.model_rebuild()
GetGOATSObservationsObservationsMatchesTargetEnvironmentFirstScienceTarget.model_rebuild()
GetGOATSObservationsObservationsMatchesTargetEnvironmentFirstScienceTargetSidereal.model_rebuild()
GetGOATSObservationsObservationsMatchesTargetEnvironmentFirstScienceTargetSiderealProperMotion.model_rebuild()
GetGOATSObservationsObservationsMatchesTargetEnvironmentFirstScienceTargetSourceProfile.model_rebuild()
GetGOATSObservationsObservationsMatchesTargetEnvironmentFirstScienceTargetSourceProfilePoint.model_rebuild()
GetGOATSObservationsObservationsMatchesTargetEnvironmentFirstScienceTargetSourceProfilePointBandNormalized.model_rebuild()
GetGOATSObservationsObservationsMatchesPosAngleConstraint.model_rebuild()
GetGOATSObservationsObservationsMatchesScienceRequirements.model_rebuild()
GetGOATSObservationsObservationsMatchesScienceRequirementsSpectroscopy.model_rebuild()
GetGOATSObservationsObservationsMatchesScienceRequirementsExposureTimeMode.model_rebuild()
GetGOATSObservationsObservationsMatchesScienceRequirementsExposureTimeModeSignalToNoise.model_rebuild()
GetGOATSObservationsObservationsMatchesScienceRequirementsExposureTimeModeTimeAndCount.model_rebuild()
GetGOATSObservationsObservationsMatchesObservingMode.model_rebuild()
GetGOATSObservationsObservationsMatchesObservingModeGmosNorthLongSlit.model_rebuild()
GetGOATSObservationsObservationsMatchesObservingModeGmosSouthLongSlit.model_rebuild()
