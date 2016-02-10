from ophyd import (EpicsSignal, EpicsSignalRO, Component as Cpt)

from .. import (RecordBase, _register_record_type)


@_register_record_type('motor')
class MotorRecord(RecordBase):
    _rtyp = 'motor'
    alarm_status = Cpt(EpicsSignalRO, '.STAT')
    at_home = Cpt(EpicsSignalRO, '.ATHM')
    card_number = Cpt(EpicsSignalRO, '.CARD')
    code_version = Cpt(EpicsSignalRO, '.VERS')
    dial_desired_value_egu = Cpt(EpicsSignal, '.DVAL')
    dial_readback_value = Cpt(EpicsSignalRO, '.DRBV')
    difference_dval_drbv = Cpt(EpicsSignalRO, '.DIFF')
    difference_rval_rrbv = Cpt(EpicsSignalRO, '.RDIF')
    direction_of_travel = Cpt(EpicsSignalRO, '.TDIR')
    freeze_offset = Cpt(EpicsSignal, '.FOF')
    home_forward = Cpt(EpicsSignal, '.HOMF')
    home_reverse = Cpt(EpicsSignal, '.HOMR')
    jog_motor_forward = Cpt(EpicsSignal, '.JOGF')
    jog_motor_reverse = Cpt(EpicsSignal, '.JOGR')
    last_dial_des_val_egu = Cpt(EpicsSignalRO, '.LDVL')
    last_raw_des_val_steps = Cpt(EpicsSignalRO, '.LRVL')
    last_rel_value_egu = Cpt(EpicsSignalRO, '.LRLV')
    last_spmg = Cpt(EpicsSignalRO, '.LSPG')
    last_user_des_val_egu = Cpt(EpicsSignalRO, '.LVAL')
    last_val_monitored = Cpt(EpicsSignalRO, '.MLST')
    last_value_archived = Cpt(EpicsSignalRO, '.ALST')
    limit_violation = Cpt(EpicsSignalRO, '.LVIO')
    monitor_mask = Cpt(EpicsSignalRO, '.MMAP')
    monitor_mask_more = Cpt(EpicsSignalRO, '.NMAP')
    motion_in_progress = Cpt(EpicsSignalRO, '.MIP')
    motor_status = Cpt(EpicsSignalRO, '.MSTA')
    motor_is_moving = Cpt(EpicsSignalRO, '.MOVN')
    post_process_command = Cpt(EpicsSignalRO, '.PP')
    ran_out_of_retries = Cpt(EpicsSignalRO, '.MISS')
    raw_desired_value_step = Cpt(EpicsSignal, '.RVAL')
    raw_encoder_position = Cpt(EpicsSignalRO, '.REP')
    raw_high_limit_switch = Cpt(EpicsSignalRO, '.RHLS')
    raw_low_limit_switch = Cpt(EpicsSignalRO, '.RLLS')
    raw_motor_position = Cpt(EpicsSignalRO, '.RMP')
    raw_readback_value = Cpt(EpicsSignalRO, '.RRBV')
    raw_cmnd_direction = Cpt(EpicsSignalRO, '.CDIR')
    relative_value_egu = Cpt(EpicsSignal, '.RLV')
    retry_count = Cpt(EpicsSignalRO, '.RCNT')
    set_set_mode = Cpt(EpicsSignal, '.SSET')
    set_use_mode = Cpt(EpicsSignal, '.SUSE')
    set_use_switch = Cpt(EpicsSignal, '.SET')
    stop = Cpt(EpicsSignal, '.STOP')
    stop_pause_move_go = Cpt(EpicsSignal, '.SPMG')
    sync_position = Cpt(EpicsSignal, '.SYNC')
    tweak_motor_forward = Cpt(EpicsSignal, '.TWF')
    tweak_motor_reverse = Cpt(EpicsSignal, '.TWR')
    user_high_limit = Cpt(EpicsSignal, '.HLM')
    user_high_limit_switch = Cpt(EpicsSignalRO, '.HLS')
    user_low_limit = Cpt(EpicsSignal, '.LLM')
    user_low_limit_switch = Cpt(EpicsSignalRO, '.LLS')
    user_offset_egu = Cpt(EpicsSignal, '.OFF')
    user_readback_value = Cpt(EpicsSignalRO, '.RBV')
    variable_offset = Cpt(EpicsSignal, '.VOF')

    # - common
    archive_deadband = Cpt(EpicsSignal, '.ADEL')
    bl_distance_egu = Cpt(EpicsSignal, '.BDST')
    bl_seconds_to_velocity = Cpt(EpicsSignal, '.BACC')
    bl_speed_rps = Cpt(EpicsSignal, '.SBAK')
    bl_velocity_egu_s = Cpt(EpicsSignal, '.BVEL')
    base_speed_rps = Cpt(EpicsSignal, '.SBAS')
    base_velocity_egu_s = Cpt(EpicsSignal, '.VBAS')
    dmov_input_link = Cpt(EpicsSignal, '.DINP')
    derivative_gain = Cpt(EpicsSignal, '.DCOF')
    desired_output_loc = Cpt(EpicsSignal, '.DOL')
    dial_high_limit = Cpt(EpicsSignal, '.DHLM')
    dial_low_limit = Cpt(EpicsSignal, '.DLLM')
    display_precision = Cpt(EpicsSignal, '.PREC')
    done_moving_to_value = Cpt(EpicsSignalRO, '.DMOV')
    egu_s_per_revolution = Cpt(EpicsSignal, '.UREV')
    enable_control = Cpt(EpicsSignal, '.CNEN')
    encoder_step_size_egu = Cpt(EpicsSignal, '.ERES')
    engineering_units = Cpt(EpicsSignal, '.EGU')
    hw_limit_violation_svr = Cpt(EpicsSignal, '.HLSV')
    high_alarm_limit_egu = Cpt(EpicsSignal, '.HIGH')
    high_operating_range = Cpt(EpicsSignal, '.HOPR')
    high_severity = Cpt(EpicsSignal, '.HSV')
    hihi_alarm_limit_egu = Cpt(EpicsSignal, '.HIHI')
    hihi_severity = Cpt(EpicsSignal, '.HHSV')
    home_velocity_egu_s = Cpt(EpicsSignal, '.HVEL')
    integral_gain = Cpt(EpicsSignal, '.ICOF')
    jog_accel_egu_s_2 = Cpt(EpicsSignal, '.JAR')
    jog_velocity_egu_s = Cpt(EpicsSignal, '.JVEL')
    lolo_alarm_limit_egu = Cpt(EpicsSignal, '.LOLO')
    lolo_severity = Cpt(EpicsSignal, '.LLSV')
    low_alarm_limit_egu = Cpt(EpicsSignal, '.LOW')
    low_operating_range = Cpt(EpicsSignal, '.LOPR')
    low_severity = Cpt(EpicsSignal, '.LSV')
    max_retry_count = Cpt(EpicsSignal, '.RTRY')
    max_speed_rps = Cpt(EpicsSignal, '.SMAX')
    max_velocity_egu_s = Cpt(EpicsSignal, '.VMAX')
    monitor_deadband = Cpt(EpicsSignal, '.MDEL')
    motor_step_size_egu = Cpt(EpicsSignal, '.MRES')
    move_fraction = Cpt(EpicsSignal, '.FRAC')
    ntm_deadband_factor = Cpt(EpicsSignal, '.NTMF')
    new_target_monitor = Cpt(EpicsSignal, '.NTM')
    offset_freeze_switch = Cpt(EpicsSignal, '.FOFF')
    output_mode_select = Cpt(EpicsSignal, '.OMSL')
    output_specification = Cpt(EpicsSignal, '.OUT')
    post_move_commands = Cpt(EpicsSignal, '.POST')
    pre_move_commands = Cpt(EpicsSignal, '.PREM')
    proportional_gain = Cpt(EpicsSignal, '.PCOF')
    rmp_input_link = Cpt(EpicsSignal, '.RINP')
    raw_velocity = Cpt(EpicsSignalRO, '.RVEL')
    readback_location = Cpt(EpicsSignal, '.RDBL')
    readback_outlink = Cpt(EpicsSignal, '.RLNK')
    readback_step_size_egu = Cpt(EpicsSignal, '.RRES')
    readback_settle_time_s = Cpt(EpicsSignal, '.DLY')
    retry_deadband_egu = Cpt(EpicsSignal, '.RDBD')
    retry_mode = Cpt(EpicsSignal, '.RMOD')
    stop_outlink = Cpt(EpicsSignal, '.STOO')
    seconds_to_velocity = Cpt(EpicsSignal, '.ACCL')
    soft_channel_position_lock = Cpt(EpicsSignal, '.LOCK')
    speed_revolutions_sec = Cpt(EpicsSignal, '.S')
    startup_commands = Cpt(EpicsSignal, '.INIT')
    status_update = Cpt(EpicsSignal, '.STUP')
    steps_per_revolution = Cpt(EpicsSignal, '.SREV')
    tweak_step_size_egu = Cpt(EpicsSignal, '.TWV')
    use_encoder_if_present = Cpt(EpicsSignal, '.UEIP')
    use_rdbl_link_if_presen = Cpt(EpicsSignal, '.URIP')
    user_direction = Cpt(EpicsSignal, '.DIR')
    velocity_egu_s = Cpt(EpicsSignal, '.VELO')
