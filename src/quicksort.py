# Python program for implementation of Selection
# Sort
from datetime import datetime
import sys

# Traverse through all array elements
def quicksort(A):
  for i in range(len(A)):

    # Find the minimum element in remaining
    # unsorted array
    min_idx = i
    for j in range(i+1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j

    # Swap the found minimum element with
    # the first element
    A[i], A[min_idx] = A[min_idx], A[i]

array = [6209,2663,4132,2074,4603,3735,5169,4627,6290,76,5259,4356,3263,6311,3496,1010,5382,2042,427,6724,5467,5529,4844,6426,524,6032,6275,4174,3184,6492,5851,4803,2356,6411,2543,1199,2043,1603,17,6844,2472,4084,1112,339,4514,3694,496,952,6390,4049,1986,1909,2728,883,2314,1813,1767,2008,2273,2254,5660,2088,2969,4450,413,3688,607,2364,581,4644,1622,2117,2088,5867,6163,2674,1783,876,6477,4321,1446,5675,4499,5016,2149,2348,6631,152,2656,3451,3241,130,1386,5026,449,3245,1025,507,2518,3137,2254,991,4480,755,1240,6294,1651,3323,5350,3093,2307,584,6528,4980,4024,6134,3990,506,314,2534,405,1772,5804,6740,3399,5959,2740,3978,6740,6666,4608,3466,3338,2176,4491,4366,5155,4884,6034,1176,5923,3281,1445,431,6435,4798,4632,3176,6827,4877,3313,1643,4015,2432,4413,448,1407,2493,1629,3420,4974,1296,425,6372,2760,3449,1960,6784,5400,4399,5013,1348,4792,6919,3990,6143,6400,6383,1734,4369,3747,4551,1734,4243,334,2268,6932,2482,3629,4079,2851,2171,3353,5578,1403,5131,6258,2240,5661,4264,2573,5631,6035,5490,4449,2328,5577,4940,10,1058,5035,5770,2804,2610,6418,910,2210,4236,837,6998,3294,4507,5882,1178,2858,6897,2401,3466,2661,580,4457,696,5690,3798,3822,6641,5174,5442,6413,1618,2812,2966,812,530,126,4781,2067,5055,5030,973,2333,6368,1896,5783,4315,3221,3860,6412,925,1221,6896,5724,6810,6885,1997,5986,2159,149,1753,4078,1943,4668,3324,2486,4445,4126,340,1584,3843,6590,970,5951,4277,5193,5224,129,6525,5838,2511,4976,1120,2683,6300,2196,5538,6678,4301,3858,5912,2267,6092,4995,4447,495,5159,5996,3218,3668,6130,6690,3574,1548,4251,436,3140,2443,2909,6764,6784,1123,5601,2547,1805,5506,2759,2429,4105,5739,414,4581,6544,6578,1322,6171,3002,6640,5873,1633,2459,5700,4281,3716,2857,4307,667,4192,927,3067,3031,1983,6966,5461,5351,5057,4428,1794,1256,3156,3101,6097,692,1492,266,487,6683,5758,6909,4731,5097,1204,2969,582,3335,1975,5377,1129,885,3217,3133,6150,6570,4718,5332,6918,203,5657,4900,4008,4274,5507,6905,5301,6056,4495,526,6882,275,4205,667,6938,5162,1142,6702,6819,2355,4272,2268,1030,4006,1132,5688,2714,2222,1953,2485,5414,1224,6322,6295,23,2829,3753,1796,1630,358,2118,4522,553,5296,3443,1844,6176,2592,6326,798,6283,2797,2210,3981,266,186,6719,2733,28,3872,1935,5271,6215,5053,3418,3556,6090,4372,5729,1388,3024,3671,5607,2397,6656,540,6715,6605,5253,3185,1164,695,6948,5929,1962,806,1020,6304,4486,2265,976,5330,2912,378,5394,6087,5036,4371,2899,959,4801,2480,5695,5323,5794,6956,3538,440,3272,6473,6888,923,5647,2468,4282,811,5604,553,1348,6456,3286,5825,2472,1836,5318,1439,6393,1626,5433,6925,1637,4231,2893,6131,6227,1561,5061,829,5195,3971,6876,4750,1193,196,2702,6033,119,1321,1803,1299,2316,5290,5757,4362,2524,896,6009,5508,2988,1393,6518,747,5546,3085,6300,3459,3665,6862,1536,2228,5264,6183,1427,846,217,922,4799,45,2925,6525,3598,3545,5037,4947,4497,1584,533,4183,3115,1170,4994,2329,1569,543,1675,5536,172,2510,716,4860,4423,891,2909,77,2607,6465,5752,4500,1759,2369,5368,93,4187,568,351,6397,6368,4165,2334,4013,2548,1482,6447,5482,3970,911,2187,245,1566,1389,1525,2098,4188,3776,4563,4042,167,767,5947,402,1052,804,5990,6771,3574,4929,299,1176,3149,6722,6422,6819,6196,6096,6484,2026,549,6529,4259,1292,4648,6492,6906,2310,2654,2662,572,2670,3991,3577,6950,459,6938,6895,3503,5577,5362,5020,6097,87,3081,278,2649,6218,6814,1835,6527,462,1254,1505,6171,3009,3036,6934,6836,5278,5476,4463,3313,6803,1745,1818,6515,1442,2552,4819,2957,3064,5265,175,5372,2433,4260,1058,1088,6536,5798,1855,1188,2667,4012,1566,655,4817,6859,3923,6361,648,5410,655,4551,2360,2468,6714,4288,340,1757,5706,1298,4592,5459,4661,6511,2795,5112,2768,3431,615,3945,2127,4881,4794,5653,2240,5888,5370,3943,5960,2263,4469,1696,794,6567,2194,1885,1012,4952,4863,6989,5381,1689,4656,151,297,110,1748,2054,2086,1249,1985,4189,1427,113,1078,4590,5464,1714,6022,1515,1253,5636,5115,3609,1348,5398,3153,5248,2544,436,1532,1517,3805,4280,4003,3108,216,6291,5497,3324,1040,2670,3367,1076,1204,3845,277,3006,2338,2085,31,5513,6822,2964,4131,3515,3050,3314,245,1720,6532,4507,3158,2558,5304,5076,5952,827,380,2236,932,946,4670,776,4645,3328,1569,39,5539,1742,6456,2475,6696,1967,672,1715,877,1401,3969,1701,969,3924,747,4820,3543,943,5833,5960,5709,5819,4890,166,2715,4070,4346,6829,4232,3326,1365,3168,2718,2380,6306,3151,1460,3838,702,3420,6850,1773,215,4823,2835,537,1048,1731,3512,2902,4623,6913,5374,2471,3085,4344,2236,4094,3422,6455,6706,6911,5528,976,4773,6843,1420,1741,6961,4079,2768,285,563,3214,4843,6597,4375,4153,4686,2577,6947,321,2246,2274,3154,2791,2378,977,497,2150,716,2436,1249,1138,547,4783,1763,1324,6507,3878,6451,1657,1564,2064,5938,2143,5846,3893,51,4880,83,6574,854,3448,6302,6927,6109,1078,1545,2381,1171,5026,1514,4580,6435,1137,2687,1372,5880,4864,2641,2811,2049,3458,1688,2277,4959,4084,4245,3151,2266,6381,966,3675,3222,4544,2193,471,5510,154,185,193,1735,1429,2870,923,4984,2132,1738,2858,4311,6748,6223,6951,482,3973,1093,6834,6329,6034,6078,1493,6034,2501,37,4815,5498,6225,2536,6045,3930,5598,3931,1978,2841,4052,1401,4349,6728,123,2692,2861,1295,3054,2873,2060,3300,5080,6982,154,4560,4681,4356,5616,4747,3920,6712,3019,3107,3237,3512,4134,5191,2791,3744,5047,3363,4895,5974,6123,3382,3328,3164,3696,3638,5095,5168,2643,4538,2289,2874,826,6211,3573,3562,4255,1341,6005,2391,5135,752,1477,5970,3777,547,5467,5940,1561,4618,4764,6975,1609,1997,5965,4604,4558,6271,2076,4935,3593,1982,5430,2735,2512,5056,5687,620,1066,5299,2241,651,4138,4379,1019,6607,6437,1480,6830,1005,4406,1871,2636,5051,1898,5326,4853,1250,1088,818,4975,2925,972,4835,4010,6693,1165,1477,4518,62,4400,2496,1284,5735,3948,3527,6391,211,3993,1317,1084,384,5292,2902,2448,1169,4185,2250,2306,6990,4896,4024,5382,2895,3986,379,723,2574,353,1744,4055,6970,3241,1733,3225,3254,70,1296,6745,7000,6794,6671,5310,6727,6651,5007,2227,3932,3438,1992,3809,5115,6992,6364,2104,536,340,985,966,1683,405,1790,537,3471,3104,4134,511,4739,5697,1406,6970,5202,5180,178,1178,1086,2600,3498,2725,4247,1407,1756,3417,3518,2472,1733,2681,2695,905,6463,3966,2529,192,6139,5844,344,67,5589,3816,6268,6384,2564,3486,5352,939,4167,5038,4004,5769,578,2645,6599,5791,602,3221,3735,2536,2504,3200,574,1083,882,5127,1137,1353,2971,2624,2405,3587,5032,2271,2824,451,895,6852,4004,1266,6212,1665,5528,5982,6106,5152,1943,1487,248,4596,4839,1426,6072,2450,3557,378,3509,3787,6328,6008,6088,5285,899,1931,5003,2142,4596,3925,6969,6534,2130,3400,1031,6989,1791,1424,4941,3237,3662,1774,259,4805,2412,4647,1703,3228,3491,70,1125,4736,5656,6775,5014,1336,1918,5178,1745,4289,3101,4773,1328,3986,4231,1223,6406,434,1078,693,2812,2271,3771,4252,4186,3450,4166,1741,6180,6335,2200,2458,6404,1338,3537,1427,3462,885,5712,5971,1853,4342,2996,2783,4640,6415,6936,6683,5015,1040,5070,517,218,3644,825,735,6867,3300,5963,5906,527,2589,1555,6417,3922,5790,5541,2074,1533,3662,5064,2996,158,5932,4943,6371,6163,4555,4449,526,2120,4878,2057,3544,1792,1922,4918,6465,2540,6301,5830,737,2536,2650,2729,5517,1310,6717,1961,1621,3343,1523,861,1910,4546,935,5282,6064,6225,2773,944,2736,4260,4891,4846,3326,2105,4937,3082,2591,2934,5606,6071,2458,2500,6460,4541,3689,603,1934,1120,1074,2956,1856,1597,2661,2705,1903,2441,170,2198,2439,4106,2413,1108,466,4759,744,6252,2236,1877,6906,3481,6755,4422,3084,3230,5141,5433,3099,5086,2859,6029,3065,6930,5395,3794,981,3646,4948,3746,1487,4258,6907,6810,4450,6828,6964,3624,4668,4173,5238,5973,4309,4153,6621,2371,480,518,1178,4209,1433,1288,1461,3607,5501,3687,6497,3459,73,382,5259,26,317,5695,14,2218,6901,1134,4291,786,4995,683,6733,5764,5707,5053,4217,5080,3061,1879,1148,1859,6543,3099,527,4423,2855,3022,1095,387,1511,427,1095,1062,4000,5249,5987,3905,5651,2126,3257,828,1064,319,2636,1233,4953,4733,5037,896,2605,890,3706,1947,3841,1550,5693,847,4980,5049,28,621,1052,3312,6069,5087,4009,2366,3588,4169,1367,5335,4192,3236,5582,4669,6872,6135,4680,2218,5031,5716,5873,1269,2577,4444,5832,5504,2848,1676,2813,5416,2741,4752,2951,6871,2960,6678,1294,1142,6601,5206,6575,4968,590,556,1573,656,309,6533,3723,6793,5597,6056,1313,3498,4034,4124,1090,3537,2810,191,3273,4119,4978,6762,4792,5809,5773,4372,2823,3668,4421,3640,6205,2057,1192,4537,572,4830,1578,599,6622,6892,3516,2294,3008,5539,1314,6354,681,5172,2498,1306,5407,1858,3296,143,1989,630,2343,957,4846,944,5477,2300,4553,4669,324,6751,3868,6426,4644,1346,6866,6125,3230,1546,710,3719,3252,1300,159,5789,5988,2675,6048,6733,6556,998,3808,124,493,1217,3877,3926,4383,5464,2626,1889,3161,6727,1480,3591,3986,1757,1520,6794,3748,6103,5752,4296,4155,6105,6762,6043,1107,5454,3952,5201,1475,2076,2872,900,1300,2280,3334,5663,6409,2204,4602,2095,3874,6849,1815,5849,4020,2082,6269,3905,319,772,2749,6698,1163,3995,691,4120,2845,806,5639,1432,468,5215,1835,3329,3995,2872,3397,4640,4411,1176,3616,754,5187,5068,1991,6447,3534,4511,2608,4083,5443,3613,5595,2648,3788,4312,5234,6271,3391,6203,2524,3181,2133,1538,4580,2196,2552,1007,4005,4053,6942,6384,130,1769,5685,6760,5656,3417,4006,3793,1828,3284,3842,1390,474,2354,5783,3036,1640,4731,4949,2966,4894,3433,2219,6139,4084,1717,5585,477,2693,5145,6748,6972,2953,6255,896,3167,5228,1224,6650,4402,371,3641,1762,3544,5993,5779,4208,5821,4942,692,789,1236,5807,5338,393,1858,2202,4402,1269,281,3080,1204,3454,1747,4074,6002,4138,6097,2450,1753,5336,3426,2291,3527,4388,6551,5667,5020,2348,6677,5919,6910,5361,2827,3055,1072,2064,6333,6567,534,5234,6617,6200,2519,1198,4647,3941,5797,3372,2704,2024,3506,769,4945,4362,1077,96,6377,4879,2073,120,3502,5555,3694,2189,1152,3044,396,2565,2669,6166,2271,6047,1363,4430,5971,5785,6721,4905,1291,693,3111,454,5309,6693,693,2077,1800,1231,4341,6096,1468,2191,3543,5999,6156,4014,3419,5516,4991,1731,5452,6811,1504,1360,2434,4008,1113,3335,2828,3050,90,625,2505,5159,3569,5679,4261,3269,4841,3187,5687,2171,314,4878,5543,3324,2761,5816,494,1776,955,2803,2981,6409,5201,2685,1730,262,6115,1168,4088,6942,1300,6905,3886,3593,1347,1534,4864,437,3328,209,502,2398,1462,3693,1976,6893,1823,5908,3339,2486,1397,182,569,6482,1447,6886,438,1904,3500,101,6640,5614,6270,2586,6916,2639,6475,2839,3687,1796,4427,3513,4359,1839,1614,5339,256,4838,4686,2170,3481,2905,4812,3344,6611,1830,1066,103,3091,3360,1597,6837,6565,5796,2062,1633,3766,4979,3872,2997,239,4940,977,3483,5549,1195,1041,2029,5573,1914,1395,3773,6451,1194,3134,4990,3233,1410,4150,1229,4833,4156,4065,3191,6943,5725,2412,4958,5447,1280,5746,5601,153,2696,4750,5355,6184,282,1482,4578,6428,4660,647,1837,5985,292,2635,4803,5455,4318,4633,1515,1405,6232,1092,315,3160,1717,2271,6257,6504,2323,5731,6487,3235,5275,3836,5303,4439,5424,2910,759,6199,624,1816,1510,5224,3091,3803,201,717,1100,4424,1447,1034,4870,1720,2180,6807,5519,4589,4194,2691,4518,6708,4732,294,5112,6000,1906,2064,3119,1566,3522,906,2063,6248,2115,1483,163,3528]

tiempoInicial = datetime.now()
quicksort(array)

print ("El arreglo ordenado de forma Ascendete es:")
for i in range(len(array)):
	print("%d"%array[i])

print (datetime.now() - tiempoInicial),