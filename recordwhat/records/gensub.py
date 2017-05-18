from ophyd import (EpicsSignal, EpicsSignalRO)

from .. import (RecordBase, _register_record_type,
                FieldComponent as Cpt)




@_register_record_type('genSub')
class GensubRecord(RecordBase):
    'Autogenerated class'

    # - ""
    alarm_status = Cpt(EpicsSignalRO, '.STAT')
    old_subr_address = Cpt(EpicsSignalRO, '.OSAD')
    old_return_value = Cpt(EpicsSignalRO, '.OVAL')
    subroutine_address = Cpt(EpicsSignalRO, '.SADR')

    # - "display"
    display_precision = Cpt(EpicsSignal, '.PREC')
    version_number = Cpt(EpicsSignalRO, '.VERS')

    # - "inputs"
    input_link_a = Cpt(EpicsSignalRO, '.INPA$')
    input_link_b = Cpt(EpicsSignalRO, '.INPB$')
    input_link_c = Cpt(EpicsSignalRO, '.INPC$')
    input_link_d = Cpt(EpicsSignalRO, '.INPD$')
    input_link_e = Cpt(EpicsSignalRO, '.INPE$')
    input_link_f = Cpt(EpicsSignalRO, '.INPF$')
    input_link_g = Cpt(EpicsSignalRO, '.INPG$')
    input_link_h = Cpt(EpicsSignalRO, '.INPH$')
    input_link_i = Cpt(EpicsSignalRO, '.INPI$')
    input_link_j = Cpt(EpicsSignalRO, '.INPJ$')
    input_link_k = Cpt(EpicsSignalRO, '.INPK$')
    input_link_l = Cpt(EpicsSignalRO, '.INPL$')
    input_link_m = Cpt(EpicsSignalRO, '.INPM$')
    input_link_n = Cpt(EpicsSignalRO, '.INPN$')
    input_link_o = Cpt(EpicsSignalRO, '.INPO$')
    input_link_p = Cpt(EpicsSignalRO, '.INPP$')
    input_link_q = Cpt(EpicsSignalRO, '.INPQ$')
    input_link_r = Cpt(EpicsSignalRO, '.INPR$')
    input_link_s = Cpt(EpicsSignalRO, '.INPS$')
    input_link_t = Cpt(EpicsSignalRO, '.INPT$')
    input_link_u = Cpt(EpicsSignalRO, '.INPU$')
    subroutine_input_link = Cpt(EpicsSignalRO, '.SUBL$')

    # - "output"
    event_flag = Cpt(EpicsSignal, '.EFLG')
    link_flag = Cpt(EpicsSignal, '.LFLG')
    output_link_a = Cpt(EpicsSignalRO, '.OUTA$')
    output_link_b = Cpt(EpicsSignalRO, '.OUTB$')
    output_link_c = Cpt(EpicsSignalRO, '.OUTC$')
    output_link_d = Cpt(EpicsSignalRO, '.OUTD$')
    output_link_e = Cpt(EpicsSignalRO, '.OUTE$')
    output_link_f = Cpt(EpicsSignalRO, '.OUTF$')
    output_link_g = Cpt(EpicsSignalRO, '.OUTG$')
    output_link_h = Cpt(EpicsSignalRO, '.OUTH$')
    output_link_i = Cpt(EpicsSignalRO, '.OUTI$')
    output_link_j = Cpt(EpicsSignalRO, '.OUTJ$')
    output_link_k = Cpt(EpicsSignalRO, '.OUTK$')
    output_link_l = Cpt(EpicsSignalRO, '.OUTL$')
    output_link_m = Cpt(EpicsSignalRO, '.OUTM$')
    output_link_n = Cpt(EpicsSignalRO, '.OUTN$')
    output_link_o = Cpt(EpicsSignalRO, '.OUTO$')
    output_link_p = Cpt(EpicsSignalRO, '.OUTP$')
    output_link_q = Cpt(EpicsSignalRO, '.OUTQ$')
    output_link_r = Cpt(EpicsSignalRO, '.OUTR$')
    output_link_s = Cpt(EpicsSignalRO, '.OUTS$')
    output_link_t = Cpt(EpicsSignalRO, '.OUTT$')
    output_link_u = Cpt(EpicsSignalRO, '.OUTU$')

    # - "sub"
    bad_return_severity = Cpt(EpicsSignal, '.BRSV')
    init_routine_name = Cpt(EpicsSignalRO, '.INAM$')
    input_structure_a = Cpt(EpicsSignalRO, '.UFA$')
    input_structure_b = Cpt(EpicsSignalRO, '.UFB$')
    input_structure_c = Cpt(EpicsSignalRO, '.UFC$')
    input_structure_d = Cpt(EpicsSignalRO, '.UFD$')
    input_structure_e = Cpt(EpicsSignalRO, '.UFE$')
    input_structure_f = Cpt(EpicsSignalRO, '.UFF$')
    input_structure_g = Cpt(EpicsSignalRO, '.UFG$')
    input_structure_h = Cpt(EpicsSignalRO, '.UFH$')
    input_structure_i = Cpt(EpicsSignalRO, '.UFI$')
    input_structure_j = Cpt(EpicsSignalRO, '.UFJ$')
    input_structure_k = Cpt(EpicsSignalRO, '.UFK$')
    input_structure_l = Cpt(EpicsSignalRO, '.UFL$')
    input_structure_m = Cpt(EpicsSignalRO, '.UFM$')
    input_structure_n = Cpt(EpicsSignalRO, '.UFN$')
    input_structure_o = Cpt(EpicsSignalRO, '.UFO$')
    input_structure_p = Cpt(EpicsSignalRO, '.UFP$')
    input_structure_q = Cpt(EpicsSignalRO, '.UFQ$')
    input_structure_r = Cpt(EpicsSignalRO, '.UFR$')
    input_structure_s = Cpt(EpicsSignalRO, '.UFS$')
    input_structure_t = Cpt(EpicsSignalRO, '.UFT$')
    input_structure_u = Cpt(EpicsSignalRO, '.UFU$')
    old_subroutine_name = Cpt(EpicsSignalRO, '.ONAM$')
    output_structure_a = Cpt(EpicsSignalRO, '.UFVA$')
    output_structure_b = Cpt(EpicsSignalRO, '.UFVB$')
    output_structure_c = Cpt(EpicsSignalRO, '.UFVC$')
    output_structure_d = Cpt(EpicsSignalRO, '.UFVD$')
    output_structure_e = Cpt(EpicsSignalRO, '.UFVE$')
    output_structure_f = Cpt(EpicsSignalRO, '.UFVF$')
    output_structure_g = Cpt(EpicsSignalRO, '.UFVG$')
    output_structure_h = Cpt(EpicsSignalRO, '.UFVH$')
    output_structure_i = Cpt(EpicsSignalRO, '.UFVI$')
    output_structure_j = Cpt(EpicsSignalRO, '.UFVJ$')
    output_structure_k = Cpt(EpicsSignalRO, '.UFVK$')
    output_structure_l = Cpt(EpicsSignalRO, '.UFVL$')
    output_structure_m = Cpt(EpicsSignalRO, '.UFVM$')
    output_structure_n = Cpt(EpicsSignalRO, '.UFVN$')
    output_structure_o = Cpt(EpicsSignalRO, '.UFVO$')
    output_structure_p = Cpt(EpicsSignalRO, '.UFVP$')
    output_structure_q = Cpt(EpicsSignalRO, '.UFVQ$')
    output_structure_r = Cpt(EpicsSignalRO, '.UFVR$')
    output_structure_s = Cpt(EpicsSignalRO, '.UFVS$')
    output_structure_t = Cpt(EpicsSignalRO, '.UFVT$')
    output_structure_u = Cpt(EpicsSignalRO, '.UFVU$')
    process_subr_name = Cpt(EpicsSignal, '.SNAM$')

    # - "wave"
    no_in_a = Cpt(EpicsSignalRO, '.NOA')
    no_in_b = Cpt(EpicsSignalRO, '.NOB')
    no_in_c = Cpt(EpicsSignalRO, '.NOC')
    no_in_d = Cpt(EpicsSignalRO, '.NOD')
    no_in_e = Cpt(EpicsSignalRO, '.NOE')
    no_in_f = Cpt(EpicsSignalRO, '.NOF')
    no_in_g = Cpt(EpicsSignalRO, '.NOG')
    no_in_h = Cpt(EpicsSignalRO, '.NOH')
    no_in_i = Cpt(EpicsSignalRO, '.NOI')
    no_in_j = Cpt(EpicsSignalRO, '.NOJ')
    no_in_k = Cpt(EpicsSignalRO, '.NOK')
    no_in_l = Cpt(EpicsSignalRO, '.NOL')
    no_in_m = Cpt(EpicsSignalRO, '.NOM')
    no_in_n = Cpt(EpicsSignalRO, '.NON')
    no_in_o = Cpt(EpicsSignalRO, '.NOO')
    no_in_p = Cpt(EpicsSignalRO, '.NOP')
    no_in_q = Cpt(EpicsSignalRO, '.NOQ')
    no_in_r = Cpt(EpicsSignalRO, '.NOR')
    no_in_s = Cpt(EpicsSignalRO, '.NOS')
    no_in_t = Cpt(EpicsSignalRO, '.NOT')
    no_in_u = Cpt(EpicsSignalRO, '.NOU')
    no_in_vala = Cpt(EpicsSignalRO, '.NOVA')
    no_in_valb = Cpt(EpicsSignalRO, '.NOVB')
    no_in_valc = Cpt(EpicsSignalRO, '.NOVC')
    no_in_vald = Cpt(EpicsSignalRO, '.NOVD')
    no_in_vale = Cpt(EpicsSignalRO, '.NOVE')
    no_in_valf = Cpt(EpicsSignalRO, '.NOVF')
    no_in_valg = Cpt(EpicsSignalRO, '.NOVG')
    no_in_vali = Cpt(EpicsSignalRO, '.NOVI')
    no_in_valj = Cpt(EpicsSignalRO, '.NOVJ')
    no_in_valk = Cpt(EpicsSignalRO, '.NOVK')
    no_in_vall = Cpt(EpicsSignalRO, '.NOVL')
    no_in_valm = Cpt(EpicsSignalRO, '.NOVM')
    no_in_valn = Cpt(EpicsSignalRO, '.NOVN')
    no_in_valo = Cpt(EpicsSignalRO, '.NOVO')
    no_in_valp = Cpt(EpicsSignalRO, '.NOVP')
    no_in_valq = Cpt(EpicsSignalRO, '.NOVQ')
    no_in_valr = Cpt(EpicsSignalRO, '.NOVR')
    no_in_vals = Cpt(EpicsSignalRO, '.NOVS')
    no_in_valt = Cpt(EpicsSignalRO, '.NOVT')
    no_in_valu = Cpt(EpicsSignalRO, '.NOVU')
    no_in_valh = Cpt(EpicsSignalRO, '.NOVH')
    total_bytes_for_vala = Cpt(EpicsSignalRO, '.TOVA')
    total_bytes_for_valb = Cpt(EpicsSignalRO, '.TOVB')
    total_bytes_for_valc = Cpt(EpicsSignalRO, '.TOVC')
    total_bytes_for_vald = Cpt(EpicsSignalRO, '.TOVD')
    total_bytes_for_vale = Cpt(EpicsSignalRO, '.TOVE')
    total_bytes_for_valf = Cpt(EpicsSignalRO, '.TOVF')
    total_bytes_for_valg = Cpt(EpicsSignalRO, '.TOVG')
    total_bytes_for_vali = Cpt(EpicsSignalRO, '.TOVI')
    total_bytes_for_valj = Cpt(EpicsSignalRO, '.TOVJ')
    total_bytes_for_valk = Cpt(EpicsSignalRO, '.TOVK')
    total_bytes_for_vall = Cpt(EpicsSignalRO, '.TOVL')
    total_bytes_for_valm = Cpt(EpicsSignalRO, '.TOVM')
    total_bytes_for_valn = Cpt(EpicsSignalRO, '.TOVN')
    total_bytes_for_valo = Cpt(EpicsSignalRO, '.TOVO')
    total_bytes_for_valp = Cpt(EpicsSignalRO, '.TOVP')
    total_bytes_for_valq = Cpt(EpicsSignalRO, '.TOVQ')
    total_bytes_for_valr = Cpt(EpicsSignalRO, '.TOVR')
    total_bytes_for_vals = Cpt(EpicsSignalRO, '.TOVS')
    total_bytes_for_valt = Cpt(EpicsSignalRO, '.TOVT')
    total_bytes_for_valu = Cpt(EpicsSignalRO, '.TOVU')
    total_bytes_for_valh = Cpt(EpicsSignalRO, '.TOVH')
    type_of_a = Cpt(EpicsSignalRO, '.FTA')
    type_of_b = Cpt(EpicsSignalRO, '.FTB')
    type_of_c = Cpt(EpicsSignalRO, '.FTC')
    type_of_d = Cpt(EpicsSignalRO, '.FTD')
    type_of_e = Cpt(EpicsSignalRO, '.FTE')
    type_of_f = Cpt(EpicsSignalRO, '.FTF')
    type_of_g = Cpt(EpicsSignalRO, '.FTG')
    type_of_h = Cpt(EpicsSignalRO, '.FTH')
    type_of_i = Cpt(EpicsSignalRO, '.FTI')
    type_of_j = Cpt(EpicsSignalRO, '.FTJ')
    type_of_k = Cpt(EpicsSignalRO, '.FTK')
    type_of_l = Cpt(EpicsSignalRO, '.FTL')
    type_of_m = Cpt(EpicsSignalRO, '.FTM')
    type_of_n = Cpt(EpicsSignalRO, '.FTN')
    type_of_o = Cpt(EpicsSignalRO, '.FTO')
    type_of_p = Cpt(EpicsSignalRO, '.FTP')
    type_of_q = Cpt(EpicsSignalRO, '.FTQ')
    type_of_r = Cpt(EpicsSignalRO, '.FTR')
    type_of_s = Cpt(EpicsSignalRO, '.FTS')
    type_of_t = Cpt(EpicsSignalRO, '.FTT')
    type_of_u = Cpt(EpicsSignalRO, '.FTU')
    type_of_vala = Cpt(EpicsSignalRO, '.FTVA')
    type_of_valb = Cpt(EpicsSignalRO, '.FTVB')
    type_of_valc = Cpt(EpicsSignalRO, '.FTVC')
    type_of_vald = Cpt(EpicsSignalRO, '.FTVD')
    type_of_vale = Cpt(EpicsSignalRO, '.FTVE')
    type_of_valf = Cpt(EpicsSignalRO, '.FTVF')
    type_of_valg = Cpt(EpicsSignalRO, '.FTVG')
    type_of_valh = Cpt(EpicsSignalRO, '.FTVH')
    type_of_vali = Cpt(EpicsSignalRO, '.FTVI')
    type_of_valj = Cpt(EpicsSignalRO, '.FTVJ')
    type_of_valk = Cpt(EpicsSignalRO, '.FTVK')
    type_of_vall = Cpt(EpicsSignalRO, '.FTVL')
    type_of_valm = Cpt(EpicsSignalRO, '.FTVM')
    type_of_valn = Cpt(EpicsSignalRO, '.FTVN')
    type_of_valo = Cpt(EpicsSignalRO, '.FTVO')
    type_of_valp = Cpt(EpicsSignalRO, '.FTVP')
    type_of_valq = Cpt(EpicsSignalRO, '.FTVQ')
    type_of_valr = Cpt(EpicsSignalRO, '.FTVR')
    type_of_vals = Cpt(EpicsSignalRO, '.FTVS')
    type_of_valt = Cpt(EpicsSignalRO, '.FTVT')
    type_of_valu = Cpt(EpicsSignalRO, '.FTVU')