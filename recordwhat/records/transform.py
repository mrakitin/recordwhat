from ophyd import (EpicsSignal, EpicsSignalRO, Component as Cpt)

from .. import (RecordBase, _register_record_type)


@_register_record_type('transform')
class TransformRecord(RecordBase):
    _rtyp = 'transform'
    alarm_status = Cpt(EpicsSignalRO, '.STAT')
    calc_invalid = Cpt(EpicsSignal, '.CAV')
    calc_invalid_cbv = Cpt(EpicsSignal, '.CBV')
    calc_invalid_ccv = Cpt(EpicsSignal, '.CCV')
    calc_invalid_cdv = Cpt(EpicsSignal, '.CDV')
    calc_invalid_cev = Cpt(EpicsSignal, '.CEV')
    calc_invalid_cfv = Cpt(EpicsSignal, '.CFV')
    calc_invalid_cgv = Cpt(EpicsSignal, '.CGV')
    calc_invalid_chv = Cpt(EpicsSignal, '.CHV')
    calc_invalid_civ = Cpt(EpicsSignal, '.CIV')
    calc_invalid_cjv = Cpt(EpicsSignal, '.CJV')
    calc_invalid_ckv = Cpt(EpicsSignal, '.CKV')
    calc_invalid_clv = Cpt(EpicsSignal, '.CLV')
    calc_invalid_cmv = Cpt(EpicsSignal, '.CMV')
    calc_invalid_cnv = Cpt(EpicsSignal, '.CNV')
    calc_invalid_cov = Cpt(EpicsSignal, '.COV')
    calc_invalid_cpv = Cpt(EpicsSignal, '.CPV')
    code_version = Cpt(EpicsSignalRO, '.VERS')
    input_link_valid = Cpt(EpicsSignalRO, '.IAV')
    input_link_valid_ibv = Cpt(EpicsSignalRO, '.IBV')
    input_link_valid_icv = Cpt(EpicsSignalRO, '.ICV')
    input_link_valid_idv = Cpt(EpicsSignalRO, '.IDV')
    input_link_valid_iev = Cpt(EpicsSignalRO, '.IEV')
    input_link_valid_ifv = Cpt(EpicsSignalRO, '.IFV')
    input_link_valid_igv = Cpt(EpicsSignalRO, '.IGV')
    input_link_valid_ihv = Cpt(EpicsSignalRO, '.IHV')
    input_link_valid_iiv = Cpt(EpicsSignalRO, '.IIV')
    input_link_valid_ijv = Cpt(EpicsSignalRO, '.IJV')
    input_link_valid_ikv = Cpt(EpicsSignalRO, '.IKV')
    input_link_valid_ilv = Cpt(EpicsSignalRO, '.ILV')
    input_link_valid_imv = Cpt(EpicsSignalRO, '.IMV')
    input_link_valid_inv = Cpt(EpicsSignalRO, '.INV')
    input_link_valid_iov = Cpt(EpicsSignalRO, '.IOV')
    input_link_valid_ipv = Cpt(EpicsSignalRO, '.IPV')
    output_link_valid = Cpt(EpicsSignalRO, '.OAV')
    output_link_valid_obv = Cpt(EpicsSignalRO, '.OBV')
    output_link_valid_ocv = Cpt(EpicsSignalRO, '.OCV')
    output_link_valid_odv = Cpt(EpicsSignalRO, '.ODV')
    output_link_valid_oev = Cpt(EpicsSignalRO, '.OEV')
    output_link_valid_ofv = Cpt(EpicsSignalRO, '.OFV')
    output_link_valid_ogv = Cpt(EpicsSignalRO, '.OGV')
    output_link_valid_ohv = Cpt(EpicsSignalRO, '.OHV')
    output_link_valid_oiv = Cpt(EpicsSignalRO, '.OIV')
    output_link_valid_ojv = Cpt(EpicsSignalRO, '.OJV')
    output_link_valid_okv = Cpt(EpicsSignalRO, '.OKV')
    output_link_valid_olv = Cpt(EpicsSignalRO, '.OLV')
    output_link_valid_omv = Cpt(EpicsSignalRO, '.OMV')
    output_link_valid_onv = Cpt(EpicsSignalRO, '.ONV')
    output_link_valid_oov = Cpt(EpicsSignalRO, '.OOV')
    output_link_valid_opv = Cpt(EpicsSignalRO, '.OPV')
    prev_value_of_a = Cpt(EpicsSignalRO, '.LA')
    prev_value_of_b = Cpt(EpicsSignalRO, '.LB')
    prev_value_of_c = Cpt(EpicsSignalRO, '.LC')
    prev_value_of_d = Cpt(EpicsSignalRO, '.LD')
    prev_value_of_e = Cpt(EpicsSignalRO, '.LE')
    prev_value_of_f = Cpt(EpicsSignalRO, '.LF')
    prev_value_of_g = Cpt(EpicsSignalRO, '.LG')
    prev_value_of_h = Cpt(EpicsSignalRO, '.LH')
    prev_value_of_i = Cpt(EpicsSignalRO, '.LI')
    prev_value_of_j = Cpt(EpicsSignalRO, '.LJ')
    prev_value_of_k = Cpt(EpicsSignalRO, '.LK')
    prev_value_of_l = Cpt(EpicsSignalRO, '.LL')
    prev_value_of_m = Cpt(EpicsSignalRO, '.LM')
    prev_value_of_n = Cpt(EpicsSignalRO, '.LN')
    prev_value_of_o = Cpt(EpicsSignalRO, '.LO')
    prev_value_of_p = Cpt(EpicsSignalRO, '.LP')

    # - common
    calc_option = Cpt(EpicsSignal, '.COPT')
    calculation_a = Cpt(EpicsSignal, '.CLCA')
    calculation_b = Cpt(EpicsSignal, '.CLCB')
    calculation_c = Cpt(EpicsSignal, '.CLCC')
    calculation_d = Cpt(EpicsSignal, '.CLCD')
    calculation_e = Cpt(EpicsSignal, '.CLCE')
    calculation_f = Cpt(EpicsSignal, '.CLCF')
    calculation_g = Cpt(EpicsSignal, '.CLCG')
    calculation_h = Cpt(EpicsSignal, '.CLCH')
    calculation_i = Cpt(EpicsSignal, '.CLCI')
    calculation_j = Cpt(EpicsSignal, '.CLCJ')
    calculation_k = Cpt(EpicsSignal, '.CLCK')
    calculation_l = Cpt(EpicsSignal, '.CLCL')
    calculation_m = Cpt(EpicsSignal, '.CLCM')
    calculation_n = Cpt(EpicsSignal, '.CLCN')
    calculation_o = Cpt(EpicsSignal, '.CLCO')
    calculation_p = Cpt(EpicsSignal, '.CLCP')
    comment_a = Cpt(EpicsSignal, '.CMTA')
    comment_b = Cpt(EpicsSignal, '.CMTB')
    comment_c = Cpt(EpicsSignal, '.CMTC')
    comment_d = Cpt(EpicsSignal, '.CMTD')
    comment_e = Cpt(EpicsSignal, '.CMTE')
    comment_f = Cpt(EpicsSignal, '.CMTF')
    comment_g = Cpt(EpicsSignal, '.CMTG')
    comment_h = Cpt(EpicsSignal, '.CMTH')
    comment_i = Cpt(EpicsSignal, '.CMTI')
    comment_j = Cpt(EpicsSignal, '.CMTJ')
    comment_k = Cpt(EpicsSignal, '.CMTK')
    comment_l = Cpt(EpicsSignal, '.CMTL')
    comment_m = Cpt(EpicsSignal, '.CMTM')
    comment_n = Cpt(EpicsSignal, '.CMTN')
    comment_o = Cpt(EpicsSignal, '.CMTO')
    comment_p = Cpt(EpicsSignal, '.CMTP')
    display_precision = Cpt(EpicsSignal, '.PREC')
    input_a = Cpt(EpicsSignal, '.INPA')
    input_b = Cpt(EpicsSignal, '.INPB')
    input_c = Cpt(EpicsSignal, '.INPC')
    input_d = Cpt(EpicsSignal, '.INPD')
    input_e = Cpt(EpicsSignal, '.INPE')
    input_f = Cpt(EpicsSignal, '.INPF')
    input_g = Cpt(EpicsSignal, '.INPG')
    input_h = Cpt(EpicsSignal, '.INPH')
    input_i = Cpt(EpicsSignal, '.INPI')
    input_j = Cpt(EpicsSignal, '.INPJ')
    input_k = Cpt(EpicsSignal, '.INPK')
    input_l = Cpt(EpicsSignal, '.INPL')
    input_m = Cpt(EpicsSignal, '.INPM')
    input_n = Cpt(EpicsSignal, '.INPN')
    input_o = Cpt(EpicsSignal, '.INPO')
    input_p = Cpt(EpicsSignal, '.INPP')
    input_bitmap = Cpt(EpicsSignal, '.MAP')
    invalid_link_action = Cpt(EpicsSignal, '.IVLA')
    output_a = Cpt(EpicsSignal, '.OUTA')
    output_b = Cpt(EpicsSignal, '.OUTB')
    output_c = Cpt(EpicsSignal, '.OUTC')
    output_d = Cpt(EpicsSignal, '.OUTD')
    output_e = Cpt(EpicsSignal, '.OUTE')
    output_f = Cpt(EpicsSignal, '.OUTF')
    output_g = Cpt(EpicsSignal, '.OUTG')
    output_h = Cpt(EpicsSignal, '.OUTH')
    output_i = Cpt(EpicsSignal, '.OUTI')
    output_j = Cpt(EpicsSignal, '.OUTJ')
    output_k = Cpt(EpicsSignal, '.OUTK')
    output_l = Cpt(EpicsSignal, '.OUTL')
    output_m = Cpt(EpicsSignal, '.OUTM')
    output_n = Cpt(EpicsSignal, '.OUTN')
    output_o = Cpt(EpicsSignal, '.OUTO')
    output_p = Cpt(EpicsSignal, '.OUTP')
    units_name = Cpt(EpicsSignal, '.EGU')
    value_of_a = Cpt(EpicsSignal, '.A')
    value_of_b = Cpt(EpicsSignal, '.B')
    value_of_c = Cpt(EpicsSignal, '.C')
    value_of_d = Cpt(EpicsSignal, '.D')
    value_of_e = Cpt(EpicsSignal, '.E')
    value_of_f = Cpt(EpicsSignal, '.F')
    value_of_g = Cpt(EpicsSignal, '.G')
    value_of_h = Cpt(EpicsSignal, '.H')
    value_of_i = Cpt(EpicsSignal, '.I')
    value_of_j = Cpt(EpicsSignal, '.J')
    value_of_k = Cpt(EpicsSignal, '.K')
    value_of_l = Cpt(EpicsSignal, '.L')
    value_of_m = Cpt(EpicsSignal, '.M')
    value_of_n = Cpt(EpicsSignal, '.N')
    value_of_o = Cpt(EpicsSignal, '.O')
    value_of_p = Cpt(EpicsSignal, '.P')
