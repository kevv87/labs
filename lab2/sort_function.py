import time

lista100_numeros = [3362, 7636, 956, 8133, 3644, 1660, 7360, 438, 9549, 6306, 5664, 7844, 2581, 2665, 2755, 2988, 8423, 8841, 6835, 7668, 3140, 2916, 290, 4731, 55, 5925, 1504, 9245, 1657, 6887, 1049, 5860, 1487, 5563, 9513, 7320, 2733, 2643, 3270, 7888, 8681, 4305, 8963, 6421, 8004, 7017, 3330, 6041, 1115, 2510, 5949, 7145, 8405, 1312, 90, 6588, 8894, 8213, 4891, 9657, 7408, 8733, 7526, 4169, 5805, 5698, 9991, 216, 7531, 9349, 3658, 6701, 106, 526, 8564, 9533, 2345, 7882, 7354, 3719, 7116, 2306, 572, 723, 8943, 1421, 9622, 2879, 906, 9388, 2052, 5905, 380, 1725, 3490, 1887, 5530, 2858, 2881, 5039]
lista500_numeros =[5145, 1344, 3102, 1054, 6708, 4764, 8051, 5106, 5252, 7668, 4191, 7439, 9080, 1861, 495, 5948, 966, 5626, 4087, 6931, 4657, 3002, 8695, 998, 3980, 4351, 2356, 9302, 3599, 5862, 5468, 9440, 4821, 4417, 6584, 2243, 9407, 5687, 8278, 395, 586, 3658, 5739, 1213, 3904, 4280, 5422, 1724, 3689, 3441, 9349, 982, 2489, 4678, 232, 8812, 2852, 7703, 359, 7868, 4043, 8699, 6355, 8153, 2449, 6936, 1288, 803, 2713, 2183, 3474, 6845, 2090, 6307, 7132, 8059, 1799, 2135, 8232, 1344, 9148, 8492, 149, 4842, 6682, 9888, 4775, 8235, 3813, 8318, 9611, 2135, 763, 5032, 8025, 7807, 6393, 167, 5172, 4387, 50, 5153, 9709, 9445, 3241, 6402, 2041, 4610, 9120, 8851, 601, 8630, 5397, 5945, 3608, 3054, 1703, 5268, 5070, 8954, 5433, 5781, 9182, 7263, 7663, 2029, 4175, 9875, 3778, 2214, 1998, 129, 4823, 5203, 8952, 5800, 6609, 4448, 8672, 1080, 4889, 3263, 2140, 6346, 6003, 2123, 2596, 9395, 2466, 7045, 6846, 5045, 5678, 8863, 9199, 6274, 2800, 1430, 9695, 9963, 6998, 6524, 7889, 4676, 7142, 5564, 5326, 4885, 1416, 3801, 8015, 6304, 1485, 5960, 2793, 8735, 7913, 2461, 399, 1495, 7896, 6255, 2359, 2204, 182, 2292, 9606, 7935, 7950, 8095, 4866, 5762, 1773, 4085, 3704, 9044, 4596, 3380, 1141, 5692, 5773, 9427, 9569, 5675, 8172, 1719, 6428, 9426, 8944, 5143, 2472, 1347, 7360, 8380, 9492, 2027, 9576, 756, 3179, 2420, 7529, 7632, 9027, 9405, 7905, 9783, 8092, 3491, 8723, 7036, 427, 301, 8782, 3077, 5165, 9551, 2364, 6865, 1936, 5218, 6398, 3002, 7874, 8566, 3122, 2002, 4908, 9422, 454, 8282, 3261, 129, 6083, 8062, 3800, 6984, 2705, 7519, 7200, 4974, 6322, 1860, 6390, 3709, 5253, 8322, 9809, 8460, 8860, 3008, 877, 9594, 3445, 3181, 4695, 5011, 4973, 6054, 1883, 2204, 1392, 369, 4785, 1731, 4685, 5661, 3189, 7792, 1614, 569, 1118, 3931, 5829, 8443, 8770, 3372, 1865, 9255, 9494, 9334, 8229, 9609, 4914, 5327, 3407, 3219, 875, 3180, 6470, 7370, 6945, 3004, 1133, 8812, 448, 9926, 3728, 4761, 5469, 7750, 8478, 3287, 5894, 4923, 9321, 5468, 6026, 9904, 2167, 3392, 6864, 9774, 6918, 5325, 2437, 7092, 2266, 148, 3482, 9136, 147, 4621, 8132, 7871, 8955, 3268, 3212, 5406, 9754, 1225, 2888, 5582, 4604, 7658, 7569, 2943, 4199, 3561, 2639, 8058, 6548, 2121, 8800, 2099, 183, 3079, 6324, 4232, 8230, 6236, 5405, 9798, 3073, 1628, 9363, 8296, 7129, 8879, 5108, 5694, 5614, 1667, 6024, 140, 735, 9391, 4503, 1504, 4545, 7514, 137, 9892, 6240, 552, 2571, 8652, 9045, 4585, 8973, 7985, 1771, 157, 8114, 8550, 8351, 4664, 4196, 5536, 4426, 183, 5910, 7290, 2573, 2207, 5422, 2727, 60, 264, 8812, 2126, 1593, 3567, 7468, 9199, 2013, 2287, 904, 5733, 6762, 9889, 6079, 2166, 2285, 6715, 6656, 6373, 1366, 2121, 3551, 7579, 4089, 7377, 8769, 9750, 4629, 4655, 6804, 4912, 2273, 5283, 5654, 1384, 6490, 6583, 2016, 8938, 2234, 9498, 9423, 8238, 2777, 2399, 2328, 1567, 175, 8296, 8083, 7342, 9287, 101, 5597, 9303, 1344, 7290, 2491, 5993, 6304, 6624, 1510, 5906, 8326, 1615, 2582, 7824, 6620, 5407, 9868, 5307, 5458, 4534, 6220, 5922, 2596, 961, 4089, 9074, 4636, 9907, 9400, 1310]
lista2000_numeros = [9531, 1064, 6679, 2397, 1146, 9425, 6905, 1207, 3536, 9313, 9565, 5651, 5601, 5014, 8301, 2680, 5184, 5833, 1465, 6658, 5182, 4417, 9380, 6886, 8732, 7989, 7711, 5459, 2337, 6902, 4592, 7548, 8066, 1917, 7343, 1350, 3035, 1223, 9738, 2858, 6881, 2307, 2287, 7842, 6710, 3344, 2603, 1914, 5359, 4448, 9168, 6535, 3078, 2833, 1920, 3590, 4978, 9463, 2440, 5134, 9832, 9334, 5796, 9923, 6555, 4818, 8880, 1024, 1475, 3492, 2888, 9284, 8029, 1816, 3784, 3770, 1460, 678, 8134, 2875, 4030, 9810, 8811, 1791, 6894, 3953, 7486, 5727, 1627, 2105, 5355, 5045, 7944, 6233, 2162, 221, 166, 1395, 1413, 2768, 1577, 892, 5918, 992, 9083, 5551, 7608, 4241, 569, 8025, 374, 7778, 4466, 427, 1581, 244, 2488, 8114, 3129, 6958, 5365, 1789, 8708, 9371, 7449, 3559, 8817, 5773, 5456, 8791, 773, 8819, 9842, 9331, 9567, 360, 448, 1081, 7761, 3237, 85, 8738, 4444, 7062, 3504, 1731, 7895, 3128, 7911, 7585, 7199, 2272, 7572, 753, 5829, 4680, 7470, 8251, 7574, 6408, 3881, 1953, 1699, 3962, 6067, 3910, 1933, 5725, 5695, 7387, 6386, 2303, 3507, 6609, 8201, 4637, 268, 5957, 3604, 4135, 1631, 4789, 5729, 9025, 9493, 9557, 9683, 5156, 3842, 2626, 6400, 6889, 8788, 6421, 6996, 4759, 552, 9724, 1099, 1650, 5274, 5703, 5582, 3875, 7070, 1766, 9306, 8163, 5426, 5492, 4699, 9868, 976, 3049, 1833, 3472, 6000, 3122, 173, 6628, 8780, 6845, 2544, 6910, 2317, 2155, 5325, 5732, 1796, 1085, 2776, 6322, 7432, 7256, 3556, 8426, 3383, 7742, 6478, 7110, 2691, 2655, 1084, 9885, 6255, 1582, 8318, 4331, 5078, 1174, 4812, 98, 8144, 496, 8215, 7680, 5975, 1936, 2317, 8578, 3568, 1308, 7210, 6560, 5409, 1774, 3388, 7044, 7889, 5928, 7847, 6958, 3243, 9290, 7249, 7865, 2223, 6972, 3153, 882, 7749, 5853, 2691, 7079, 6178, 595, 5897, 3802, 3081, 3916, 8673, 7042, 9837, 662, 5735, 5752, 2540, 6882, 2275, 9841, 3162, 3395, 6903, 1386, 9306, 8094, 5170, 4978, 8559, 3061, 996, 2499, 6014, 2776, 4889, 8591, 3850, 2819, 2463, 5965, 8565, 7519, 4708, 5682, 4769, 9963, 1772, 685, 1295, 36, 5653, 9584, 7383, 5373, 7366, 2880, 1962, 8966, 6457, 1916, 9844, 1657, 1915, 7688, 1142, 666, 7956, 3964, 3045, 1163, 8834, 5929, 4899, 9256, 136, 307, 4891, 6364, 6500, 3788, 2024, 6818, 5872, 3347, 3735, 2625, 4593, 82, 8262, 3338, 7411, 161, 5739, 2428, 2985, 9260, 4591, 3162, 7978, 4123, 6126, 2694, 5388, 6082, 7107, 1946, 2986, 4555, 2472, 9705, 5614, 5186, 8992, 4794, 1963, 3089, 2446, 4241, 9140, 7487, 133, 9923, 4988, 5143, 1017, 381, 6802, 1865, 925, 1740, 1416, 7250, 6399, 8319, 8945, 8353, 9376, 6117, 3200, 5592, 9837, 8839, 6231, 3165, 647, 5211, 7085, 5523, 7560, 9760, 7318, 7657, 5381, 1872, 9378, 8121, 4685, 7129, 3265, 5997, 1854, 7147, 7584, 5858, 7472, 3587, 6599, 5906, 6129, 6356, 9266, 7438, 3595, 4459, 6940, 8581, 1846, 4556, 651, 4506, 2787, 313, 6582, 1496, 7988, 4087, 4954, 2909, 5680, 4098, 4146, 6533, 3880, 6445, 1895, 5021, 477, 411, 4731, 5640, 3904, 7390, 9468, 5051, 3195, 8398, 913, 1546, 9334, 4887, 8699, 5739, 5453, 9627, 2276, 6702, 4955, 5689, 9701, 1111, 3918, 8952, 5212, 2755, 673, 426, 8758, 8926, 3528, 5928, 2780, 2193, 6086, 3430, 6994, 2526, 1001, 953, 7772, 4557, 8600, 6185, 8398, 5221, 1165, 2542, 8172, 6440, 856, 6459, 5506, 1643, 1275, 7548, 8383, 5629, 1644, 4360, 6923, 7536, 5217, 7890, 2679, 1124, 3811, 2369, 705, 4506, 3635, 2884, 8002, 1380, 8124, 3924, 7976, 6239, 780, 6627, 8133, 5962, 5169, 9056, 1030, 1614, 5556, 6441, 3756, 1765, 6365, 1442, 2853, 7620, 8233, 8706, 5390, 7611, 1896, 4318, 6048, 6411, 5217, 4627, 8739, 1572, 8218, 6116, 2030, 4872, 235, 8060, 5569, 1411, 4920, 4846, 2289, 2659, 8981, 415, 8783, 4208, 3268, 6296, 9472, 7758, 8276, 7592, 4085, 3197, 5522, 1588, 4157, 2705, 7237, 5922, 895, 2534, 2145, 6427, 854, 8201, 2683, 2222, 609, 369, 3704, 9355, 1197, 9873, 7856, 907, 4400, 1174, 4914, 5058, 5678, 8011, 4833, 1451, 8636, 6885, 7517, 2931, 8853, 7566, 9891, 2073, 5725, 9247, 2966, 6105, 2911, 8939, 766, 5119, 5448, 4306, 6415, 3071, 289, 6406, 201, 5599, 6781, 7618, 2649, 7459, 7987, 4737, 5124, 5118, 578, 6000, 8149, 786, 6496, 315, 8839, 7311, 5064, 1202, 3938, 3917, 2740, 1132, 7572, 2509, 4527, 8928, 2441, 4840, 2287, 7940, 9256, 4475, 4815, 5226, 9531, 5695, 2893, 1367, 712, 4127, 8716, 1625, 4374, 8449, 9802, 6214, 4398, 6973, 8172, 8899, 3377, 1918, 5823, 4524, 3241, 7306, 9192, 6389, 297, 6471, 7610, 7546, 3616, 8833, 724, 2089, 5080, 7217, 8771, 740, 8429, 4760, 6320, 1692, 3095, 3764, 4593, 4746, 9281, 6385, 3608, 4093, 5860, 9783, 4458, 1810, 8500, 8572, 3886, 677, 6920, 6020, 6052, 9281, 8950, 5797, 4170, 8697, 97, 7936, 7488, 2623, 4307, 6750, 9747, 9040, 7620, 1418, 737, 5185, 4307, 1340, 1548, 64, 2130, 2467, 5561, 9801, 2985, 6776, 7121, 4855, 1045, 2304, 5692, 8599, 5736, 8646, 4159, 3543, 2808, 3741, 3501, 1662, 2393, 1305, 1771, 6402, 8404, 3640, 4420, 5990, 495, 5497, 727, 3378, 2120, 6713, 7301, 7319, 2836, 4536, 3708, 2987, 2696, 3553, 3762, 8057, 7853, 6355, 4655, 8801, 735, 2580, 6789, 5367, 4710, 8684, 9365, 3539, 7125, 776, 3122, 8857, 8628, 3362, 6218, 59, 8760, 9781, 1807, 2743, 6107, 6939, 1533, 5463, 27, 1572, 7266, 5211, 9776, 223, 2969, 3836, 2821, 8240, 845, 99, 7772, 5883, 343, 100, 5546, 6552, 7674, 2407, 671, 1870, 6239, 2195, 4173, 2753, 119, 4432, 2160, 5537, 567, 9019, 2803, 5606, 3435, 5769, 7441, 6244, 8415, 4417, 8024, 712, 937, 9981, 2931, 86, 9274, 7905, 786, 2268, 3319, 8696, 3284, 6445, 963, 8411, 3945, 6339, 2448, 6529, 9099, 8283, 9810, 7555, 2869, 8794, 9539, 2596, 6198, 7092, 2749, 4141, 5783, 3064, 5121, 2997, 9878, 5857, 7890, 8696, 595, 8735, 1487, 9102, 2136, 4085, 5759, 9060, 6535, 8124, 4059, 7609, 9330, 7113, 3432, 8866, 2793, 3579, 2927, 4319, 5098, 6724, 8737, 501, 5329, 5930, 2401, 8146, 1384, 9291, 2663, 8780, 3569, 2271, 6475, 1794, 7900, 8542, 7385, 1773, 7699, 3146, 856, 4582, 8034, 4238, 7406, 436, 4532, 8567, 9376, 528, 4856, 6164, 6530, 8465, 644, 8483, 5308, 1314, 361, 3130, 1495, 7288, 933, 7651, 2081, 5858, 7364, 4746, 7208, 8229, 4403, 2564, 1215, 7447, 2707, 8502, 8654, 471, 705, 448, 5493, 8053, 6955, 9876, 2751, 221, 1457, 2719, 9556, 13, 5732, 2121, 5360, 2738, 5904, 4496, 2014, 7579, 2577, 904, 9606, 3093, 1176, 3070, 7511, 7623, 5969, 6498, 9948, 1873, 6632, 4547, 4473, 3240, 3114, 3225, 2977, 5598, 1018, 4479, 559, 9267, 9094, 7860, 9485, 7479, 7900, 6368, 6771, 7428, 7401, 6881, 7945, 587, 2974, 1920, 37, 1346, 6856, 8435, 478, 6728, 1895, 7508, 4038, 4409, 764, 4492, 4772, 1172, 7059, 4059, 8762, 7416, 2700, 3326, 2752, 1650, 1777, 5926, 1284, 5613, 6651, 4726, 1065, 5469, 8870, 7655, 1872, 3045, 501, 4919, 4854, 6169, 912, 1639, 8013, 7955, 6840, 587, 9615, 6482, 7288, 4991, 3942, 6621, 9837, 1582, 487, 9217, 4917, 6116, 7041, 1000, 4612, 5354, 2680, 509, 5138, 9340, 4199, 2554, 6009, 7885, 4338, 4508, 8372, 5569, 3907, 5282, 2722, 1625, 7128, 8682, 5166, 7843, 672, 8814, 3450, 3399, 7085, 1914, 5502, 5908, 69, 9267, 470, 3204, 1100, 8922, 3133, 3238, 4975, 8216, 1532, 344, 2432, 9254, 1280, 623, 6745, 9403, 7334, 9783, 8443, 4215, 8667, 5930, 1174, 8561, 5037, 1612, 3468, 7310, 7258, 4048, 7437, 391, 9998, 8168, 3383, 5478, 7534, 9329, 793, 7155, 2856, 8064, 2028, 8811, 6791, 9912, 7033, 1389, 513, 3304, 4083, 5977, 1350, 4674, 5738, 2752, 3250, 7333, 1091, 46, 6162, 3701, 8052, 7929, 1497, 4939, 2291, 8944, 8745, 2046, 6634, 9212, 7916, 7404, 4496, 8964, 177, 2147, 4138, 5817, 3697, 3956, 1171, 7969, 7784, 3937, 8344, 8694, 4137, 3448, 7646, 6826, 7650, 8898, 125, 9573, 6635, 7342, 1633, 9536, 2267, 1017, 3453, 9523, 8829, 3750, 5735, 9096, 8453, 2184, 4207, 1035, 1345, 3701, 7358, 6724, 8414, 8158, 6252, 9274, 2014, 4594, 158, 9582, 7750, 1375, 9403, 8446, 3010, 1169, 5200, 3674, 8070, 1421, 6371, 1600, 3173, 9347, 6931, 3752, 3923, 2543, 4739, 8383, 5002, 7892, 309, 3465, 4340, 6045, 5579, 4067, 2711, 2, 6661, 9652, 5288, 6691, 6529, 392, 1107, 254, 6164, 8879, 6789, 6556, 5524, 7174, 8691, 2887, 5293, 3546, 6297, 969, 3641, 2409, 7233, 9432, 1043, 221, 7040, 3031, 3681, 5381, 404, 3333, 5580, 6588, 9459, 6109, 6827, 5389, 5481, 7470, 2594, 4463, 5733, 5811, 2824, 4380, 1607, 5266, 2337, 938, 8455, 6991, 9917, 8514, 6239, 6916, 2037, 3029, 4715, 4559, 1898, 2343, 5045, 4263, 5363, 2511, 4320, 8013, 2725, 9407, 7890, 4001, 1995, 513, 248, 1903, 4535, 3518, 952, 1915, 3438, 3384, 8915, 7566, 7450, 5852, 2600, 8619, 7893, 7104, 2038, 6971, 6155, 318, 7216, 1004, 5292, 4547, 465, 7039, 5244, 1632, 6603, 5873, 5726, 6073, 3040, 2680, 1747, 9372, 528, 8590, 3604, 4595, 417, 4226, 6852, 4489, 6820, 299, 7486, 2145, 5281, 6291, 3847, 36, 7355, 3721, 1057, 7590, 9206, 2182, 3743, 6742, 1512, 9957, 6853, 6654, 2324, 1394, 5536, 4345, 910, 751, 5944, 4544, 2232, 3314, 5740, 8572, 1499, 1886, 6728, 291, 9924, 5042, 8381, 3988, 1338, 8158, 6360, 4988, 5959, 2147, 2413, 3107, 1204, 9384, 1321, 2293, 1545, 8717, 3093, 4646, 5473, 3461, 6836, 441, 2488, 5277, 3404, 559, 4511, 595, 988, 8262, 2364, 8636, 6016, 3040, 4458, 9909, 859, 4772, 2112, 6970, 4398, 7967, 1479, 3267, 5787, 47, 5782, 629, 3916, 7868, 7979, 1289, 343, 6703, 8315, 8988, 4257, 4080, 4277, 288, 9850, 1508, 4730, 7828, 748, 7127, 5259, 485, 7338, 3115, 2282, 7693, 2962, 7512, 4802, 5309, 612, 8152, 6343, 4245, 9695, 4563, 1814, 3607, 3783, 404, 9726, 9623, 3934, 5596, 6951, 4664, 8899, 5658, 4103, 6400, 9662, 492, 4753, 1954, 4964, 7963, 4403, 7428, 9661, 1840, 2866, 6401, 8927, 7660, 1828, 5562, 5850, 5160, 5963, 7424, 7766, 4630, 9033, 5312, 4642, 143, 4586, 8660, 375, 3101, 504, 2134, 6104, 2354, 6563, 3407, 809, 6549, 374, 1303, 8832, 8398, 1831, 4780, 106, 7843, 7673, 8844, 8451, 4468, 9100, 3665, 4147, 8916, 7228, 8874, 8393, 4355, 8527, 193, 7123, 6429, 3199, 6822, 6760, 7622, 5910, 8673, 5601, 2459, 6391, 8047, 8514, 7670, 1366, 1576, 9744, 7441, 9362, 4697, 5394, 306, 9992, 8697, 5899, 855, 661, 4500, 7050, 9698, 3035, 9610, 6946, 4902, 983, 9578, 2223, 6200, 2997, 331, 4412, 908, 1644, 2017, 230, 2453, 1331, 799, 5841, 5186, 5128, 4299, 172, 8726, 3802, 6640, 1196, 4189, 798, 7440, 9800, 2948, 5773, 7018, 9418, 6841, 5083, 7499, 4422, 513, 8450, 924, 1052, 3460, 5814, 7052, 661, 2400, 8240, 9579, 5342, 7201, 627, 4436, 59, 3430, 5857, 5801, 9839, 7984, 818, 7215, 8366, 782, 975, 8317, 9936, 811, 2500, 3819, 718, 4845, 8394, 7904, 4161, 3905, 1535, 5946, 283, 8329, 5052, 8946, 7903, 7793, 1134, 7587, 3286, 5705, 3273, 6994, 2432, 1747, 4888, 421, 2304, 9510, 1532, 7550, 8527, 5856, 931, 4397, 7635, 1343, 8257, 5043, 8400, 2796, 2160, 7654, 9234, 7455, 5444, 4921, 2507, 1597, 2071, 6510, 3259, 5354, 2874, 4201, 4805, 2882, 2170, 2061, 2341, 5555, 7230, 9004, 2241, 2290, 1362, 8644, 3585, 8152, 5620, 6142, 2791, 3452, 6032, 179, 4424, 6279, 3641, 8486, 3876, 5486, 5675, 2558, 2057, 7142, 890, 5690, 4222, 3196, 499, 1799, 1501, 4578, 6323, 1638, 3542, 9843, 2906, 5778, 5954, 4677, 8296, 1939, 9092, 5984, 6681, 6191, 2810, 1777, 8653, 884, 3554, 8040, 6258, 1712, 6910, 5910, 9654, 9184, 5106, 7005, 5872, 2557, 269, 5457, 2859, 7850, 356, 3671, 5792, 8861, 9931, 835, 1774, 5768, 7144, 5738, 6652, 9039, 9158, 8193, 8591, 9726, 1972, 6848, 4021, 6629, 2876, 6996, 6237, 2496, 1715, 6281, 472, 7076, 4221, 6505, 118, 875, 6020, 9192, 2245, 1569, 9996, 9721, 6583, 3162, 3229, 8334, 8859, 6903, 7206, 7345, 5296, 6153, 9407, 3937, 6282, 7592, 721, 2797, 3100, 4465, 3117, 7496, 4314, 3741, 9499, 4200, 1623, 2408, 3621, 1066, 3762, 8344, 2570, 6130, 289, 1729, 4324, 4305, 7223, 5837, 9442, 4079, 2578, 7906, 5703, 1154, 2919, 2323, 8782, 6187, 5917, 3970, 2033, 734, 5986, 5911, 638, 3330, 2093, 2520, 65, 1959, 8173, 5578, 7636, 5990, 8113, 465, 9394, 8332, 4460, 3938, 1478, 4431, 9876, 6507, 5275, 2370, 4491, 1469, 2311, 4686, 9686, 8338, 1988, 9497, 6663, 1037, 7460, 1682, 5607, 1472, 455, 3816, 9772, 279, 6282, 6580, 9967, 7759, 5436, 2738, 1135, 8086, 7158, 7910, 3374, 6676, 9231, 9475, 1759, 9935, 7003, 8276, 278, 8410, 5658, 8551]

start = time.clock()
lista100_numeros_ordenada = sorted(lista100_numeros)
end = time.clock()
print('Funcion sort')
print('Ordena 100 numeros en %s segundos, la lista ordenada es: \n%s' % (end-start, lista100_numeros_ordenada))
print('\n')

start = time.clock()
lista500_numeros_ordenada = sorted(lista500_numeros)
end = time.clock()
print('Ordena 500 numeros en %s segundos, la lista ordenada es: \n%s' % (end-start, lista500_numeros_ordenada))
print('\n')

start = time.clock()
lista1000_numeros_ordenada = sorted(lista1000_numeros)
end = time.clock()
print('Ordena 1000 numeros en %s segundos, la lista ordenada es: \n%s' % (end-start, lista1000_numeros_ordenada))
print('\n')

start = time.clock()
lista2000_numeros_ordenada = sorted(lista2000_numeros)
end = time.clock()
print('Ordena 2000 numeros en %s segundos, la lista ordenada es: \n%s' % (end-start, lista2000_numeros_ordenada))
