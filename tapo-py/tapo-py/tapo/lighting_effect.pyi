from typing import Optional

class LightingEffectType(StrEnum):
    Sequence = "sequence"
    Random = "random"
    Pulse = "pulse"
    Static = "static"

class LightingEffect:
    """Lighting effect."""

    brightness: int
    is_custom: bool
    display_colors: list[int]
    enabled: bool
    id: str
    name: str
    type: LightingEffectType
    backgrounds: Optional[list[int]]
    brightness_range: Optional[list[int]]
    direction: Optional[int]
    duration: Optional[int]
    expansion_strategy: Optional[int]
    fadeoff: Optional[int]
    hue_range: Optional[list[int]]
    init_states: Optional[list[int]]
    random_seed: Optional[int]
    repeat_times: Optional[int]
    run_time: Optional[int]
    saturation_range: Optional[list[int]]
    segment_length: Optional[int]
    segments: Optional[list[int]]
    sequence: Optional[list[int]]
    spread: Optional[int]
    transition: Optional[int]
    transition_range: Optional[list[int]]
    transition_sequence: Optional[list[int]]

    def new(id: str, name: str, type: LightingEffectType, custom: bool, enable: bool, brightness: int, display_colors: list[int]) -> LightingEffect:
        """"""

    def new_with_random_id(name: str, type: LightingEffectType, custom: bool, enable: bool, brightness: int, display_colors: list[int]) -> LightingEffect:
        """"""

    def with_brightness(self: LightingEffect, brightness: int) -> LightingEffect:
        """"""

    def with_is_custom(self: LightingEffect, is_custom: bool) -> LightingEffect:
        """"""

    def with_display_colors(self: LightingEffect, display_colors: list[int]) -> LightingEffect:
        """"""

    def with_enabled(self: LightingEffect, enabled: bool) -> LightingEffect:
        """"""

    def with_id(self: LightingEffect, id: str) -> LightingEffect:
        """"""

    def with_name(self: LightingEffect, name: str) -> LightingEffect:
        """"""

    def with_type(self: LightingEffect, type: LightingEffectType) -> LightingEffect:
        """"""

    def with_backgrounds(self: LightingEffect, backgrounds: list[int]) -> LightingEffect:
        """"""

    def with_brightness_range(self: LightingEffect, brightness_range: list[int]) -> LightingEffect:
        """"""

    def with_init_states(self: LightingEffect, init_states: list[int]) -> LightingEffect:
        """"""

    def with_direction(self: LightingEffect, direction: int) -> LightingEffect:
        """"""

    def with_duration(self: LightingEffect, duration: int) -> LightingEffect:
        """"""

    def with_expansion_strategy(self: LightingEffect, expansion_strategy: int) -> LightingEffect:
        """"""

    def with_fadeoff(self: LightingEffect, fadeoff: int) -> LightingEffect:
        """"""

    def with_hue_range(self: LightingEffect, hue_range: list[int]) -> LightingEffect:
        """"""

    def with_random_seed(self: LightingEffect, random_seed: int) -> LightingEffect:
        """"""

    def with_repeat_times(self: LightingEffect, repeat_times: int) -> LightingEffect:
        """"""

    def with_run_time(self: LightingEffect, run_time: int) -> LightingEffect:
        """"""

    def with_saturation_range(self: LightingEffect, saturation_range: list[int]) -> LightingEffect:
        """"""

    def with_segment_length(self: LightingEffect, segment_length: int) -> LightingEffect:
        """"""

    def with_segments(self: LightingEffect, segments: list[int]) -> LightingEffect:
        """"""

    def with_sequence(self: LightingEffect, sequence: list[int]) -> LightingEffect:
        """"""

    def with_spread(self: LightingEffect, spread: int) -> LightingEffect:
        """"""

    def with_transition(self: LightingEffect, transition: int) -> LightingEffect:
        """"""

    def with_transition_range(self: LightingEffect, transition_range: list[int]) -> LightingEffect:
        """"""

    def with_transition_sequence(self: LightingEffect, transition_sequence: list[int]) -> LightingEffect:
        """"""
