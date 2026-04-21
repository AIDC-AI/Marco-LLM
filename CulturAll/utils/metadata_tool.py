# Topic list
topics = {
    "Belief",
    "Commerce",
    "Education",
    "Entertainment",
    "Finance",
    "Food",
    "Government",
    "Habitat",
    "Health",
    "Heritage",
    "Language",
    "Pets",
    "Science",
    "Social",
    "Travel",
    "Work",
}
assert len(topics) == 16

# Language list
lcode2name = {
    "am": "Amharic",
    "ar": "Arabic",
    "as": "Assamese",
    "az": "Azerbaijani",
    "be": "Belarusian",
    "bg": "Bulgarian",
    "bn": "Bengali",
    "bs": "Bosnian",
    "cs": "Czech",
    "de": "German",
    "el": "Greek",
    "en": "English",
    "es": "Spanish",
    "et": "Estonian",
    "eu": "Basque",
    "fa": "Persian",
    "fi": "Finnish",
    "fj": "Fijian",
    "fr": "French",
    "ha": "Hausa",
    "he": "Hebrew",
    "hi": "Hindi",
    "hr": "Croatian",
    "hu": "Hungarian",
    "hy": "Armenian",
    "id": "Indonesian",
    "it": "Italian",
    "ja": "Japanese",
    "ka": "Georgian",
    "kk": "Kazakh",
    "km": "Khmer",
    "ko": "Korean",
    "lo": "Lao",
    "lt": "Lithuanian",
    "mk": "Macedonian",
    "ml": "Malayalam",
    "ms": "Malay",
    "mt": "Maltese",
    "my": "Burmese",
    "ne": "Nepali",
    "nl": "Dutch",
    "pl": "Polish",
    "pt": "Portuguese",
    "rn": "Rundi",
    "ro": "Romanian",
    "ru": "Russian",
    "si": "Sinhala",
    "sm": "Samoan",
    "sn": "Shona",
    "so": "Somali",
    "sq": "Albanian",
    "sr": "Serbian",
    "su": "Sundanese",
    "sv": "Swedish",
    "sw": "Swahili",
    "ta": "Tamil",
    "te": "Telugu",
    "th": "Thai",
    "tl": "Tagalog",
    "to": "Tongan",
    "tr": "Turkish",
    "uk": "Ukrainian",
    "ur": "Urdu",
    "uz": "Uzbek",
    "vi": "Vietnamese",
    "zh": "Chinese",
}
name2lcode = {v: k for k, v in lcode2name.items()}

ccode2name = {
    # 5 000-plus
    "in": "India",
    "es": "Spain",
    "cn": "China",
    "id": "Indonesia",
    "kr": "South Korea",
    # 1 000-plus
    "us": "United States",
    "ir": "Iran",
    "gr": "Greece",
    "az": "Azerbaijan",
    "fr": "France",
    "ph": "Philippines",
    "jp": "Japan",
    "ru": "Russia",
    "il": "Israel",
    "sa": "Saudi Arabia",
    "hu": "Hungary",
    "mx": "Mexico",
    "it": "Italy",
    "tr": "Turkey",
    "vn": "Vietnam",
    "nl": "Netherlands",
    "ua": "Ukraine",
    "pl": "Poland",
    "np": "Nepal",
    "bd": "Bangladesh",
    "et": "Ethiopia",
    "my": "Malaysia",
    "pt": "Portugal",
    "rs": "Serbia",
    "mk": "North Macedonia",
    "hr": "Croatia",
    "ng": "Nigeria",
    # 500-plus
    "al": "Albania",
    "fi": "Finland",
    "uz": "Uzbekistan",
    "am": "Armenia",
    "dz": "Algeria",
    "ge": "Georgia",
    "kz": "Kazakhstan",
    "lt": "Lithuania",
    "bg": "Bulgaria",
    "by": "Belarus",
    "kp": "North Korea",
    "uk": "United Kingdom",  # non-standard ISO, kept because it appears in data
    # 300-plus
    "pk": "Pakistan",
    "de": "Germany",
    "ee": "Estonia",
    "sg": "Singapore",
    # 150-plus
    "za": "South Africa",
    "hk": "Hong Kong",
    "ar": "Argentina",
    "th": "Thailand",
    "ke": "Kenya",
    # double-digit
    "cl": "Chile",
    "br": "Brazil",
    "eg": "Egypt",
    "tw": "Taiwan",
    "nz": "New Zealand",
    "zw": "Zimbabwe",
    # "gb": "United Kingdom",
    "pe": "Peru",
    "ro": "Romania",
    "lb": "Lebanon",
    "sd": "Sudan",
    "so": "Somalia",
    "mm": "Myanmar",
    "ie": "Ireland",
    "af": "Afghanistan",
    "au": "Australia",
    "mu": "Mauritius",
    "bi": "Burundi",
    "ca": "Canada",
    "kh": "Cambodia",
    "tl": "Timor-Leste",
    "mt": "Malta",
    "ws": "Samoa",
    "se": "Sweden",
    "to": "Tonga",
    "lk": "Sri Lanka",
    "cy": "Cyprus",
    "ba": "Bosnia and Herzegovina",
    "pg": "Papua New Guinea",
    "ve": "Venezuela",
    "iq": "Iraq",
    "ps": "Palestine",
    "la": "Laos",
    "at": "Austria",
    "co": "Colombia",
    "ss": "South Sudan",
    "cz": "Czech Republic",
    "fj": "Fiji",
    "sy": "Syria",
    "ma": "Morocco",
    "do": "Dominican Republic",
    "ec": "Ecuador",
    "cr": "Costa Rica",
    "py": "Paraguay",
    "sv": "El Salvador",
}
name2ccode = {v: k for k, v in ccode2name.items()}

ccode2name_zh = {
    # 5 000+
    "in": "印度",
    "es": "西班牙",
    "cn": "中国",
    "id": "印度尼西亚",
    "kr": "韩国",
    # 1 000+
    "us": "美国",
    "ir": "伊朗",
    "gr": "希腊",
    "az": "阿塞拜疆",
    "fr": "法国",
    "ph": "菲律宾",
    "jp": "日本",
    "ru": "俄罗斯",
    "il": "以色列",
    "sa": "沙特阿拉伯",
    "hu": "匈牙利",
    "mx": "墨西哥",
    "it": "意大利",
    "tr": "土耳其",
    "vn": "越南",
    "nl": "荷兰",
    "ua": "乌克兰",
    "pl": "波兰",
    "np": "尼泊尔",
    "bd": "孟加拉国",
    "et": "埃塞俄比亚",
    "my": "马来西亚",
    "pt": "葡萄牙",
    "rs": "塞尔维亚",
    "mk": "北马其顿",
    "hr": "克罗地亚",
    "ng": "尼日利亚",
    # 500+
    "al": "阿尔巴尼亚",
    "fi": "芬兰",
    "uz": "乌兹别克斯坦",
    "am": "亚美尼亚",
    "dz": "阿尔及利亚",
    "ge": "格鲁吉亚",
    "kz": "哈萨克斯坦",
    "lt": "立陶宛",
    "bg": "保加利亚",
    "by": "白俄罗斯",
    "kp": "朝鲜",
    "uk": "英国",  # 数据中出现的 uk，等同于 gb
    # 300+
    "pk": "巴基斯坦",
    "de": "德国",
    "ee": "爱沙尼亚",
    "sg": "新加坡",
    # 150+
    "za": "南非",
    "hk": "香港",
    "ar": "阿根廷",
    "th": "泰国",
    "ke": "肯尼亚",
    # 100 以下到双位数
    "cl": "智利",
    "br": "巴西",
    "eg": "埃及",
    "tw": "台湾",
    "nz": "新西兰",
    "zw": "津巴布韦",
    # "gb": "英国",
    "pe": "秘鲁",
    "ro": "罗马尼亚",
    "lb": "黎巴嫩",
    "sd": "苏丹",
    "so": "索马里",
    "mm": "缅甸",
    "ie": "爱尔兰",
    "af": "阿富汗",
    "au": "澳大利亚",
    "mu": "毛里求斯",
    "bi": "布隆迪",
    "ca": "加拿大",
    "kh": "柬埔寨",
    "tl": "东帝汶",
    "mt": "马耳他",
    "ws": "萨摩亚",
    "se": "瑞典",
    "to": "汤加",
    "lk": "斯里兰卡",
    "cy": "塞浦路斯",
    "ba": "波斯尼亚和黑塞哥维那",
    "pg": "巴布亚新几内亚",
    "ve": "委内瑞拉",
    "iq": "伊拉克",
    "ps": "巴勒斯坦",
    "la": "老挝",
    "at": "奥地利",
    "co": "哥伦比亚",
    "ss": "南苏丹",
    "cz": "捷克",
    "fj": "斐济",
    "sy": "叙利亚",
    "ma": "摩洛哥",
}
name2ccode_zh = {v: k for k, v in ccode2name_zh.items()}

lcode2ccode = {
    "am": "et",  # Amharic - Ethiopia
    "ar": "sa",  # Arabic - Saudi Arabia
    "as": "in",  # Assamese - India
    "az": "az",  # Azerbaijani - Azerbaijan
    "be": "by",  # Belarusian - Belarus
    "bg": "bg",  # Bulgarian - Bulgaria
    "bn": "bd",  # Bengali - Bangladesh (more Bengali speakers in Bangladesh than India)
    "bs": "ba",  # Bosnian - Bosnia and Herzegovina
    "cs": "cz",  # Czech - Czech Republic
    "de": "de",  # German - Germany
    "el": "gr",  # Greek - Greece
    "en": "us",  # English - United States (most English speakers globally)
    "es": "es",  # Spanish - Spain
    "et": "ee",  # Estonian - Estonia
    "eu": "es",  # Basque - Spain (Basque region)
    "fa": "ir",  # Persian (Farsi) - Iran
    "fi": "fi",  # Finnish - Finland
    "fj": "fj",  # Fijian - Fiji
    "fr": "fr",  # French - France
    "ha": "ng",  # Hausa - Nigeria
    "he": "il",  # Hebrew - Israel
    "hi": "in",  # Hindi - India
    "hr": "hr",  # Croatian - Croatia
    "hu": "hu",  # Hungarian - Hungary
    "hy": "am",  # Armenian - Armenia
    "id": "id",  # Indonesian - Indonesia
    "it": "it",  # Italian - Italy
    "ja": "jp",  # Japanese - Japan
    "ka": "ge",  # Georgian - Georgia
    "kk": "kz",  # Kazakh - Kazakhstan
    "km": "kh",  # Khmer - Cambodia
    "ko": "kr",  # Korean - South Korea
    "lo": "la",  # Lao - Laos
    "lt": "lt",  # Lithuanian - Lithuania
    "mk": "mk",  # Macedonian - North Macedonia
    "ml": "in",  # Malayalam - India
    "ms": "my",  # Malay - Malaysia
    "mt": "mt",  # Maltese - Malta
    "my": "mm",  # Burmese - Myanmar
    "ne": "np",  # Nepali - Nepal
    "nl": "nl",  # Dutch - Netherlands
    "pl": "pl",  # Polish - Poland
    "pt": "pt",  # Portuguese - Portugal
    "rn": "bi",  # Rundi - Burundi
    "ro": "ro",  # Romanian - Romania
    "ru": "ru",  # Russian - Russia
    "si": "lk",  # Sinhala - Sri Lanka
    "sm": "ws",  # Samoan - Samoa
    "sn": "zw",  # Shona - Zimbabwe
    "so": "so",  # Somali - Somalia
    "sq": "al",  # Albanian - Albania
    "sr": "rs",  # Serbian - Serbia
    "su": "id",  # Sundanese - Indonesia
    "sv": "se",  # Swedish - Sweden
    "sw": "ke",  # Swahili - Kenya
    "ta": "in",  # Tamil - India
    "te": "in",  # Telugu - India
    "th": "th",  # Thai - Thailand
    "tl": "ph",  # Tagalog - Philippines
    "to": "to",  # Tongan - Tonga
    "tr": "tr",  # Turkish - Turkey
    "uk": "ua",  # Ukrainian - Ukraine
    "ur": "pk",  # Urdu - Pakistan
    "uz": "uz",  # Uzbek - Uzbekistan
    "vi": "vn",  # Vietnamese - Vietnam
    "zh": "cn",  # Chinese - China
}

ccode2lcode = {
    # 5 000-plus
    "in": "hi",  # India - Hindi
    "es": "es",  # Spain - Spanish
    "cn": "zh",  # China - Mandarin (Chinese)
    "id": "id",  # Indonesia - Indonesian
    "kr": "ko",  # South Korea - Korean
    # 1 000-plus
    "us": "en",  # United States - English
    "ir": "fa",  # Iran - Persian (Farsi)
    "gr": "el",  # Greece - Greek
    "az": "az",  # Azerbaijan - Azerbaijani
    "fr": "fr",  # France - French
    "ph": "tl",  # Philippines - Tagalog (Filipino)
    "jp": "ja",  # Japan - Japanese
    "ru": "ru",  # Russia - Russian
    "il": "he",  # Israel - Hebrew
    "sa": "ar",  # Saudi Arabia - Arabic
    "hu": "hu",  # Hungary - Hungarian
    "mx": "es",  # Mexico - Spanish
    "it": "it",  # Italy - Italian
    "tr": "tr",  # Turkey - Turkish
    "vn": "vi",  # Vietnam - Vietnamese
    "nl": "nl",  # Netherlands - Dutch
    "ua": "uk",  # Ukraine - Ukrainian
    "pl": "pl",  # Poland - Polish
    "np": "ne",  # Nepal - Nepali
    "bd": "bn",  # Bangladesh - Bengali
    "et": "am",  # Ethiopia - Amharic
    "my": "ms",  # Malaysia - Malay
    "pt": "pt",  # Portugal - Portuguese
    "rs": "sr",  # Serbia - Serbian
    "mk": "mk",  # North Macedonia - Macedonian
    "hr": "hr",  # Croatia - Croatian
    "ng": "en",  # Nigeria - English (official, though Hausa, Yoruba, and Igbo are also widely spoken)
    # 500-plus
    "al": "sq",  # Albania - Albanian
    "fi": "fi",  # Finland - Finnish
    "uz": "uz",  # Uzbekistan - Uzbek
    "am": "hy",  # Armenia - Armenian
    "dz": "ar",  # Algeria - Arabic
    "ge": "ka",  # Georgia - Georgian
    "kz": "kk",  # Kazakhstan - Kazakh
    "lt": "lt",  # Lithuania - Lithuanian
    "bg": "bg",  # Bulgaria - Bulgarian
    "by": "be",  # Belarus - Belarusian (though Russian is widely spoken)
    "kp": "ko",  # North Korea - Korean
    "uk": "en",  # United Kingdom - English (specified as non-standard ISO in `ccode2name`)
    # 300-plus
    "pk": "ur",  # Pakistan - Urdu
    "de": "de",  # Germany - German
    "ee": "et",  # Estonia - Estonian
    "sg": "en",  # Singapore - English (Malay, Mandarin, and Tamil are also official)
    # 150-plus
    "za": "en",  # South Africa - English (though there are 11 official languages, including Zulu and Afrikaans)
    "hk": "zh",  # Hong Kong - Cantonese (Chinese)
    "ar": "es",  # Argentina - Spanish
    "th": "th",  # Thailand - Thai
    "ke": "sw",  # Kenya - Swahili (English is also official)
    # double-digit
    "cl": "es",  # Chile - Spanish
    "br": "pt",  # Brazil - Portuguese
    "eg": "ar",  # Egypt - Arabic
    "tw": "zh",  # Taiwan - Mandarin (Chinese)
    "nz": "en",  # New Zealand - English
    "zw": "en",  # Zimbabwe - English
    # "gb": "en",  # United Kingdom - English
    "pe": "es",  # Peru - Spanish
    "ro": "ro",  # Romania - Romanian
    "lb": "ar",  # Lebanon - Arabic
    "sd": "ar",  # Sudan - Arabic
    "so": "so",  # Somalia - Somali
    "mm": "my",  # Myanmar - Burmese
    "ie": "en",  # Ireland - English (Irish Gaelic is also spoken)
    "af": "ps",  # Afghanistan - Pashto (Dari is also widely spoken)
    "au": "en",  # Australia - English
    "mu": "en",  # Mauritius - English (French and Creole are also widely used)
    "bi": "fr",  # Burundi - French (Kirundi is also widely spoken)
    "ca": "en",  # Canada - English (French is also official)
    "kh": "km",  # Cambodia - Khmer
    "tl": "pt",  # Timor-Leste - Portuguese (Tetum is also widely used)
    "mt": "mt",  # Malta - Maltese
    "ws": "sm",  # Samoa - Samoan
    "se": "sv",  # Sweden - Swedish
    "to": "to",  # Tonga - Tongan
    "lk": "si",  # Sri Lanka - Sinhala (Tamil is also official)
    "cy": "el",  # Cyprus - Greek
    "ba": "bs",  # Bosnia and Herzegovina - Bosnian (Croatian and Serbian are also official)
    "pg": "en",  # Papua New Guinea - English (Tok Pisin and Hiri Motu are also official)
    "ve": "es",  # Venezuela - Spanish
    "iq": "ar",  # Iraq - Arabic (Kurdish is also official in some regions)
    "ps": "ar",  # Palestine - Arabic
    "la": "lo",  # Laos - Lao
    "at": "de",  # Austria - German
    "co": "es",  # Colombia - Spanish
    "ss": "en",  # South Sudan - English
    "cz": "cs",  # Czech Republic - Czech
    "fj": "en",  # Fiji - English (Fijian and Fiji Hindi are also spoken)
    "sy": "ar",  # Syria - Arabic
    "ma": "ar",  # Morocco - Arabic
}


def get_all_topics():
    return list(topics)


def get_language_name(lang_code):
    return lcode2name.get(lang_code)


def get_language_code(lang_name):
    return name2lcode.get(lang_name)


def get_all_language_names():
    return list(lcode2name.values())


def get_all_language_codes():
    return list(lcode2name.keys())


def get_language_mapping():
    return lcode2name.copy()


def get_country_name(country_code):
    return ccode2name.get(country_code)


def get_country_code(country_name):
    return name2ccode.get(country_name)


def get_all_country_names():
    return list(ccode2name.values())


def get_all_country_codes():
    return list(ccode2name.keys())


def get_country_mapping():
    return ccode2name.copy()


def get_country_name_zh(country_code):
    return ccode2name_zh.get(country_code)


def get_country_code_zh(country_name):
    return name2ccode_zh.get(country_name)


def get_all_country_names_zh():
    return list(ccode2name_zh.values())


def get_all_country_codes_zh():
    return list(ccode2name_zh.keys())


def get_country_mapping_zh():
    return ccode2name_zh.copy()


def get_most_common_country(language_code):
    return lcode2ccode.get(language_code)


def get_most_common_country_name(language_code):
    return ccode2name.get(lcode2ccode.get(language_code))


def get_all_most_common_country():
    return list(lcode2ccode.values())


def get_most_common_language(country_code):
    return ccode2lcode.get(country_code)


def get_most_common_language_name(country_code):
    return lcode2name.get(ccode2lcode.get(country_code))


def get_all_most_common_language():
    return list(ccode2lcode.values())
