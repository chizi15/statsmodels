import numpy as np

est = dict(
    rank=13,
    N=758,
    Q=.0150568875809373,
    J=11.41312078635046,
    J_df=2,
    k_1=13,
    converged=1,
    has_xtinst=0,
    type=1,
    n_eq=1,
    k=13,
    n_moments=15,
    k_aux=13,
    k_eq_model=0,
    ic=6,
    k_eq=13,
    cmdline="gmm (lw - {xb:s iq expr tenure rns smsa dyear*} - {b0}) , instruments(expr tenure rns smsa dyear* med kww age mrt) igmm",  # noqa:E501
    cmd="gmm",
    estat_cmd="gmm_estat",
    predict="gmm_p",
    marginsnotok="_ALL",
    eqnames="1",
    technique="gn",
    winit="Unadjusted",
    estimator="igmm",
    wmatrix="robust",
    vce="robust",
    vcetype="Robust",
    params="xb_s xb_iq xb_expr xb_tenure xb_rns xb_smsa xb_dyear_67 xb_dyear_68 xb_dyear_69 xb_dyear_70 xb_dyear_71 xb_dyear_73 b0",  # noqa:E501
    inst_1="expr tenure rns smsa dyear_67 dyear_68 dyear_69 dyear_70 dyear_71 dyear_73 med kww age mrt _cons",  # noqa:E501
    params_1="xb_s xb_iq xb_expr xb_tenure xb_rns xb_smsa xb_dyear_67 xb_dyear_68 xb_dyear_69 xb_dyear_70 xb_dyear_71 xb_dyear_73 b0",  # noqa:E501
    sexp_1="lw - ({xb_s} *s + {xb_iq} *iq + {xb_expr} *expr + {xb_tenure} *tenure + {xb_rns} *rns + {xb_smsa} *smsa + {xb_dyear_67} *dyear_67 + {xb_dyear_68} *dyear_68 + {xb_dyear_69} *dyear_69 + {xb_dyear_70} *dyear_70 + {xb_dyear_71} *dyear_71 + {xb_dyear_73} *dyear_73) - {b0}",  # noqa:E501
    properties="b V",
)

params_table = np.array([
    .17587739850768,  .02085563162829,  8.4330890400415,  3.366583555e-17,
    .1350011116414,  .21675368537396, np.nan,  1.9599639845401,
    0, -.00928586712743,  .00491894287617,   -1.88777697997,
    .05905589683705, -.01892681800673,  .00035508375188, np.nan,
    1.9599639845401,                0,  .05031651549731,  .00810558790493,
    6.2076330659127,  5.378855978e-10,  .03442985513012,   .0662031758645,
    np.nan,  1.9599639845401,                0,  .04246235782951,
    .00956418082077,  4.4397276280375,  9.007280073e-06,  .02371690787918,
    .06120780777985, np.nan,  1.9599639845401,                0,
    -.1039476753865,  .03373281188749, -3.0815004611293,  .00205960157647,
    -.17006277178325, -.03783257898975, np.nan,  1.9599639845401,
    0,  .12477256813508,  .03099244898605,  4.0259021864082,
    .0000567572801,  .06402848432973,  .18551665194043, np.nan,
    1.9599639845401,                0, -.05297127223127,   .0517946935923,
    -1.0227162003936,  .30644204936546, -.15448700626247,  .04854446179993,
    np.nan,  1.9599639845401,                0,  .04564516152971,
    .05001865637643,  .91256272831865,  .36147256434055, -.05238960352318,
    .1436799265826, np.nan,  1.9599639845401,                0,
    .15574543741982,  .04802004585645,  3.2433421218593,  .00118136262363,
    .06162787700523,  .24986299783442, np.nan,  1.9599639845401,
    0,  .16681173496168,  .06134387289984,  2.7192892635594,
    .00654223677971,   .0465799534058,  .28704351651757, np.nan,
    1.9599639845401,                0,  .08417610675323,  .05582688740597,
    1.507805838092,  .13160422753823, -.02524258193145,  .19359479543791,
    np.nan,  1.9599639845401,                0,  .09964580476612,
    .06124947866865,  1.6268841291727,  .10376170930541, -.02040096749628,
    .21969257702853, np.nan,  1.9599639845401,                0,
    4.0027753075622,  .33649589464938,  11.895465505554,  1.249543428e-32,
    3.3432554731038,  4.6622951420205, np.nan,  1.9599639845401,
    0]).reshape(13, 9)

params_table_colnames = 'b se z pvalue ll ul df crit eform'.split()

params_table_rownames = ['_cons'] * 13

cov = np.array([
    .00043495737061, -.00007938790704,  .00002809207919,  .00001486824321,
    -.00017806650894, -6.696078938e-06, -.00011595347261, -.00018816769626,
    -.00012205118386, -.00008281236274, -.00031504876539, -.00063574245306,
    .00264272738846, -.00007938790704,  .00002419599902,  4.932871670e-06,
    -.00001114848619,  .00006618803917, -.00002202930782,  4.808220835e-07,
    .00003206765662, -.00002261059773, -.00006024105579, -.00001412126593,
    .00001474591556, -.00144330101198,  .00002809207919,  4.932871670e-06,
    .00006570055528,  -.0000203894891,  .00005213529923, -.00003297805448,
    .00003595284891,  .00008758906787,  .00003058926358,  .00001696423798,
    -.00008568569767, -.00013140753648, -.00094326672008,  .00001486824321,
    -.00001114848619,  -.0000203894891,  .00009147355477, -.00003774547245,
    7.828122784e-06,  .00008484461309,  .00006729820252,  .00011236802193,
    .00010082715772,  .00011217081931,  .00009440153548,  .00075659901252,
    -.00017806650894,  .00006618803917,  .00005213529923, -.00003774547245,
    .00113790259784,  .00013005865302,  .00018021354375,  .00018779266096,
    -9.435310865e-06,   .0000165483542, -.00005323328914,  .00008265052168,
    -.00499436873124, -6.696078938e-06, -.00002202930782, -.00003297805448,
    7.828122784e-06,  .00013005865302,  .00096053189415,  .00005704546746,
    .00011160225767,  .00025285680201,  .00010656723202,  .00030213005331,
    .00030792696913,  .00157128168902, -.00011595347261,  4.808220835e-07,
    .00003595284891,  .00008484461309,  .00018021354375,  .00005704546746,
    .00268269028432,  .00085942321667,  .00091151417222,  .00096327250114,
    .00090372304081,  .00102768195348,  .00034563629591, -.00018816769626,
    .00003206765662,  .00008758906787,  .00006729820252,  .00018779266096,
    .00011160225767,  .00085942321667,   .0025018659857,  .00092591134763,
    .00088266305412,   .0008241186538,  .00095084381197, -.00206285154639,
    -.00012205118386, -.00002261059773,  .00003058926358,  .00011236802193,
    -9.435310865e-06,  .00025285680201,  .00091151417222,  .00092591134763,
    .00230592480406,  .00118265696692,   .0011106470199,  .00129290662149,
    .00256049741814, -.00008281236274, -.00006024105579,  .00001696423798,
    .00010082715772,   .0000165483542,  .00010656723202,  .00096327250114,
    .00088266305412,  .00118265696692,  .00376307074235,  .00124584145426,
    .00155915431219,  .00599086304364, -.00031504876539, -.00001412126593,
    -.00008568569767,  .00011217081931, -.00005323328914,  .00030213005331,
    .00090372304081,   .0008241186538,   .0011106470199,  .00124584145426,
    .00311664135744,   .0018437604357,  .00431259131307, -.00063574245306,
    .00001474591556, -.00013140753648,  .00009440153548,  .00008265052168,
    .00030792696913,  .00102768195348,  .00095084381197,  .00129290662149,
    .00155915431219,   .0018437604357,  .00375149863718,  .00538769349865,
    .00264272738846, -.00144330101198, -.00094326672008,  .00075659901252,
    -.00499436873124,  .00157128168902,  .00034563629591, -.00206285154639,
    .00256049741814,  .00599086304364,  .00431259131307,  .00538769349865,
    .11322948711589]).reshape(13, 13)

cov_colnames = ['_cons'] * 13

cov_rownames = ['_cons'] * 13


class Bunch(dict):
    def __init__(self, **kw):
        dict.__init__(self, kw)
        self.__dict__ = self

        for i, att in enumerate(['params', 'bse', 'tvalues', 'pvalues']):
            self[att] = self.params_table[:, i]


results = Bunch(
    params_table=params_table,
    params_table_colnames=params_table_colnames,
    params_table_rownames=params_table_rownames,
    cov=cov,
    cov_colnames=cov_colnames,
    cov_rownames=cov_rownames,
    **est
)
