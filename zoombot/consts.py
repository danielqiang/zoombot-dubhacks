from google.cloud import texttospeech as tts
from google.cloud.texttospeech import SsmlVoiceGender as Gender
from google.cloud.speech import RecognitionConfig
from collections import namedtuple

DEFAULT_RATE = 24000
DEFAULT_CHUNK = DEFAULT_RATE // 10  # 100ms
# DEFAULT_SAMPLE_RATE = 44100
DEFAULT_ENCODING_STT = RecognitionConfig.AudioEncoding.LINEAR16
DEFAULT_ENCODING_TTS = tts.AudioEncoding.LINEAR16

_Voice = namedtuple("Voice", ["language_code", "name", "gender", "rate"])


class Voices:
    """Container class for namedtuples representing Google Cloud
    Speech Synthesis voices"""

    class Standard:
        AR_XA_STANDARD_A = _Voice("ar-XA", "ar-XA-Standard-A", Gender.FEMALE, 24000)
        AR_XA_STANDARD_B = _Voice("ar-XA", "ar-XA-Standard-B", Gender.MALE, 24000)
        AR_XA_STANDARD_C = _Voice("ar-XA", "ar-XA-Standard-C", Gender.MALE, 24000)
        AR_XA_STANDARD_D = _Voice("ar-XA", "ar-XA-Standard-D", Gender.FEMALE, 24000)
        BN_IN_STANDARD_A = _Voice("bn-IN", "bn-IN-Standard-A", Gender.FEMALE, 24000)
        BN_IN_STANDARD_B = _Voice("bn-IN", "bn-IN-Standard-B", Gender.MALE, 24000)
        CMN_CN_STANDARD_A = _Voice("cmn-CN", "cmn-CN-Standard-A", Gender.FEMALE, 24000)
        CMN_CN_STANDARD_B = _Voice("cmn-CN", "cmn-CN-Standard-B", Gender.MALE, 24000)
        CMN_CN_STANDARD_C = _Voice("cmn-CN", "cmn-CN-Standard-C", Gender.MALE, 24000)
        CMN_CN_STANDARD_D = _Voice("cmn-CN", "cmn-CN-Standard-D", Gender.FEMALE, 24000)
        CMN_TW_STANDARD_A = _Voice("cmn-TW", "cmn-TW-Standard-A", Gender.FEMALE, 24000)
        CMN_TW_STANDARD_B = _Voice("cmn-TW", "cmn-TW-Standard-B", Gender.MALE, 24000)
        CMN_TW_STANDARD_C = _Voice("cmn-TW", "cmn-TW-Standard-C", Gender.MALE, 24000)
        CS_CZ_STANDARD_A = _Voice("cs-CZ", "cs-CZ-Standard-A", Gender.FEMALE, 24000)
        DA_DK_STANDARD_A = _Voice("da-DK", "da-DK-Standard-A", Gender.FEMALE, 24000)
        DA_DK_STANDARD_C = _Voice("da-DK", "da-DK-Standard-C", Gender.MALE, 24000)
        DA_DK_STANDARD_D = _Voice("da-DK", "da-DK-Standard-D", Gender.FEMALE, 24000)
        DA_DK_STANDARD_E = _Voice("da-DK", "da-DK-Standard-E", Gender.FEMALE, 24000)
        DE_DE_STANDARD_A = _Voice("de-DE", "de-DE-Standard-A", Gender.FEMALE, 24000)
        DE_DE_STANDARD_B = _Voice("de-DE", "de-DE-Standard-B", Gender.MALE, 24000)
        DE_DE_STANDARD_E = _Voice("de-DE", "de-DE-Standard-E", Gender.MALE, 24000)
        DE_DE_STANDARD_F = _Voice("de-DE", "de-DE-Standard-F", Gender.FEMALE, 24000)
        EL_GR_STANDARD_A = _Voice("el-GR", "el-GR-Standard-A", Gender.FEMALE, 22050)
        EN_AU_STANDARD_A = _Voice("en-AU", "en-AU-Standard-A", Gender.FEMALE, 24000)
        EN_AU_STANDARD_B = _Voice("en-AU", "en-AU-Standard-B", Gender.MALE, 24000)
        EN_AU_STANDARD_C = _Voice("en-AU", "en-AU-Standard-C", Gender.FEMALE, 24000)
        EN_AU_STANDARD_D = _Voice("en-AU", "en-AU-Standard-D", Gender.MALE, 24000)
        EN_GB_STANDARD_A = _Voice("en-GB", "en-GB-Standard-A", Gender.FEMALE, 24000)
        EN_GB_STANDARD_B = _Voice("en-GB", "en-GB-Standard-B", Gender.MALE, 24000)
        EN_GB_STANDARD_C = _Voice("en-GB", "en-GB-Standard-C", Gender.FEMALE, 24000)
        EN_GB_STANDARD_D = _Voice("en-GB", "en-GB-Standard-D", Gender.MALE, 24000)
        EN_GB_STANDARD_F = _Voice("en-GB", "en-GB-Standard-F", Gender.FEMALE, 24000)
        EN_IN_STANDARD_A = _Voice("en-IN", "en-IN-Standard-A", Gender.FEMALE, 24000)
        EN_IN_STANDARD_B = _Voice("en-IN", "en-IN-Standard-B", Gender.MALE, 24000)
        EN_IN_STANDARD_C = _Voice("en-IN", "en-IN-Standard-C", Gender.MALE, 24000)
        EN_IN_STANDARD_D = _Voice("en-IN", "en-IN-Standard-D", Gender.FEMALE, 24000)
        EN_US_STANDARD_B = _Voice("en-US", "en-US-Standard-B", Gender.MALE, 24000)
        EN_US_STANDARD_C = _Voice("en-US", "en-US-Standard-C", Gender.FEMALE, 24000)
        EN_US_STANDARD_D = _Voice("en-US", "en-US-Standard-D", Gender.MALE, 24000)
        EN_US_STANDARD_E = _Voice("en-US", "en-US-Standard-E", Gender.FEMALE, 24000)
        EN_US_STANDARD_G = _Voice("en-US", "en-US-Standard-G", Gender.FEMALE, 24000)
        EN_US_STANDARD_H = _Voice("en-US", "en-US-Standard-H", Gender.FEMALE, 24000)
        EN_US_STANDARD_I = _Voice("en-US", "en-US-Standard-I", Gender.MALE, 24000)
        EN_US_STANDARD_J = _Voice("en-US", "en-US-Standard-J", Gender.MALE, 24000)
        ES_ES_STANDARD_A = _Voice("es-ES", "es-ES-Standard-A", Gender.FEMALE, 24000)
        FIL_PH_STANDARD_A = _Voice("fil-PH", "fil-PH-Standard-A", Gender.FEMALE, 24000)
        FIL_PH_STANDARD_B = _Voice("fil-PH", "fil-PH-Standard-B", Gender.FEMALE, 24000)
        FIL_PH_STANDARD_C = _Voice("fil-PH", "fil-PH-Standard-C", Gender.MALE, 24000)
        FIL_PH_STANDARD_D = _Voice("fil-PH", "fil-PH-Standard-D", Gender.MALE, 24000)
        FI_FI_STANDARD_A = _Voice("fi-FI", "fi-FI-Standard-A", Gender.FEMALE, 24000)
        FR_CA_STANDARD_A = _Voice("fr-CA", "fr-CA-Standard-A", Gender.FEMALE, 24000)
        FR_CA_STANDARD_B = _Voice("fr-CA", "fr-CA-Standard-B", Gender.MALE, 24000)
        FR_CA_STANDARD_C = _Voice("fr-CA", "fr-CA-Standard-C", Gender.FEMALE, 24000)
        FR_CA_STANDARD_D = _Voice("fr-CA", "fr-CA-Standard-D", Gender.MALE, 24000)
        FR_FR_STANDARD_A = _Voice("fr-FR", "fr-FR-Standard-A", Gender.FEMALE, 24000)
        FR_FR_STANDARD_B = _Voice("fr-FR", "fr-FR-Standard-B", Gender.MALE, 24000)
        FR_FR_STANDARD_C = _Voice("fr-FR", "fr-FR-Standard-C", Gender.FEMALE, 24000)
        FR_FR_STANDARD_D = _Voice("fr-FR", "fr-FR-Standard-D", Gender.MALE, 24000)
        FR_FR_STANDARD_E = _Voice("fr-FR", "fr-FR-Standard-E", Gender.FEMALE, 24000)
        GU_IN_STANDARD_A = _Voice("gu-IN", "gu-IN-Standard-A", Gender.FEMALE, 24000)
        GU_IN_STANDARD_B = _Voice("gu-IN", "gu-IN-Standard-B", Gender.MALE, 24000)
        HI_IN_STANDARD_A = _Voice("hi-IN", "hi-IN-Standard-A", Gender.FEMALE, 24000)
        HI_IN_STANDARD_B = _Voice("hi-IN", "hi-IN-Standard-B", Gender.MALE, 24000)
        HI_IN_STANDARD_C = _Voice("hi-IN", "hi-IN-Standard-C", Gender.MALE, 24000)
        HI_IN_STANDARD_D = _Voice("hi-IN", "hi-IN-Standard-D", Gender.FEMALE, 24000)
        HU_HU_STANDARD_A = _Voice("hu-HU", "hu-HU-Standard-A", Gender.FEMALE, 24000)
        ID_ID_STANDARD_A = _Voice("id-ID", "id-ID-Standard-A", Gender.FEMALE, 24000)
        ID_ID_STANDARD_B = _Voice("id-ID", "id-ID-Standard-B", Gender.MALE, 24000)
        ID_ID_STANDARD_C = _Voice("id-ID", "id-ID-Standard-C", Gender.MALE, 24000)
        ID_ID_STANDARD_D = _Voice("id-ID", "id-ID-Standard-D", Gender.FEMALE, 22050)
        IT_IT_STANDARD_A = _Voice("it-IT", "it-IT-Standard-A", Gender.FEMALE, 24000)
        IT_IT_STANDARD_B = _Voice("it-IT", "it-IT-Standard-B", Gender.FEMALE, 24000)
        IT_IT_STANDARD_C = _Voice("it-IT", "it-IT-Standard-C", Gender.MALE, 24000)
        IT_IT_STANDARD_D = _Voice("it-IT", "it-IT-Standard-D", Gender.MALE, 24000)
        JA_JP_STANDARD_A = _Voice("ja-JP", "ja-JP-Standard-A", Gender.FEMALE, 24000)
        JA_JP_STANDARD_B = _Voice("ja-JP", "ja-JP-Standard-B", Gender.FEMALE, 24000)
        JA_JP_STANDARD_C = _Voice("ja-JP", "ja-JP-Standard-C", Gender.MALE, 24000)
        JA_JP_STANDARD_D = _Voice("ja-JP", "ja-JP-Standard-D", Gender.MALE, 24000)
        KN_IN_STANDARD_A = _Voice("kn-IN", "kn-IN-Standard-A", Gender.FEMALE, 24000)
        KN_IN_STANDARD_B = _Voice("kn-IN", "kn-IN-Standard-B", Gender.MALE, 24000)
        KO_KR_STANDARD_A = _Voice("ko-KR", "ko-KR-Standard-A", Gender.FEMALE, 24000)
        KO_KR_STANDARD_B = _Voice("ko-KR", "ko-KR-Standard-B", Gender.FEMALE, 24000)
        KO_KR_STANDARD_C = _Voice("ko-KR", "ko-KR-Standard-C", Gender.MALE, 24000)
        KO_KR_STANDARD_D = _Voice("ko-KR", "ko-KR-Standard-D", Gender.MALE, 24000)
        ML_IN_STANDARD_A = _Voice("ml-IN", "ml-IN-Standard-A", Gender.FEMALE, 24000)
        ML_IN_STANDARD_B = _Voice("ml-IN", "ml-IN-Standard-B", Gender.MALE, 24000)
        NB_NO_STANDARD_A = _Voice("nb-NO", "nb-NO-Standard-A", Gender.FEMALE, 24000)
        NB_NO_STANDARD_B = _Voice("nb-NO", "nb-NO-Standard-B", Gender.MALE, 24000)
        NB_NO_STANDARD_C = _Voice("nb-NO", "nb-NO-Standard-C", Gender.FEMALE, 24000)
        NB_NO_STANDARD_D = _Voice("nb-NO", "nb-NO-Standard-D", Gender.MALE, 24000)
        NB_NO_STANDARD_E = _Voice("nb-NO", "nb-no-Standard-E", Gender.FEMALE, 24000)
        NL_NL_STANDARD_A = _Voice("nl-NL", "nl-NL-Standard-A", Gender.FEMALE, 24000)
        NL_NL_STANDARD_B = _Voice("nl-NL", "nl-NL-Standard-B", Gender.MALE, 24000)
        NL_NL_STANDARD_C = _Voice("nl-NL", "nl-NL-Standard-C", Gender.MALE, 24000)
        NL_NL_STANDARD_D = _Voice("nl-NL", "nl-NL-Standard-D", Gender.FEMALE, 24000)
        NL_NL_STANDARD_E = _Voice("nl-NL", "nl-NL-Standard-E", Gender.FEMALE, 24000)
        PL_PL_STANDARD_A = _Voice("pl-PL", "pl-PL-Standard-A", Gender.FEMALE, 24000)
        PL_PL_STANDARD_B = _Voice("pl-PL", "pl-PL-Standard-B", Gender.MALE, 24000)
        PL_PL_STANDARD_C = _Voice("pl-PL", "pl-PL-Standard-C", Gender.MALE, 24000)
        PL_PL_STANDARD_D = _Voice("pl-PL", "pl-PL-Standard-D", Gender.FEMALE, 24000)
        PL_PL_STANDARD_E = _Voice("pl-PL", "pl-PL-Standard-E", Gender.FEMALE, 22050)
        PT_BR_STANDARD_A = _Voice("pt-BR", "pt-BR-Standard-A", Gender.FEMALE, 24000)
        PT_PT_STANDARD_A = _Voice("pt-PT", "pt-PT-Standard-A", Gender.FEMALE, 24000)
        PT_PT_STANDARD_B = _Voice("pt-PT", "pt-PT-Standard-B", Gender.MALE, 24000)
        PT_PT_STANDARD_C = _Voice("pt-PT", "pt-PT-Standard-C", Gender.MALE, 24000)
        PT_PT_STANDARD_D = _Voice("pt-PT", "pt-PT-Standard-D", Gender.FEMALE, 24000)
        RU_RU_STANDARD_A = _Voice("ru-RU", "ru-RU-Standard-A", Gender.FEMALE, 24000)
        RU_RU_STANDARD_B = _Voice("ru-RU", "ru-RU-Standard-B", Gender.MALE, 24000)
        RU_RU_STANDARD_C = _Voice("ru-RU", "ru-RU-Standard-C", Gender.FEMALE, 24000)
        RU_RU_STANDARD_D = _Voice("ru-RU", "ru-RU-Standard-D", Gender.MALE, 24000)
        RU_RU_STANDARD_E = _Voice("ru-RU", "ru-RU-Standard-E", Gender.FEMALE, 24000)
        SK_SK_STANDARD_A = _Voice("sk-SK", "sk-SK-Standard-A", Gender.FEMALE, 24000)
        SV_SE_STANDARD_A = _Voice("sv-SE", "sv-SE-Standard-A", Gender.FEMALE, 22050)
        TA_IN_STANDARD_A = _Voice("ta-IN", "ta-IN-Standard-A", Gender.FEMALE, 24000)
        TA_IN_STANDARD_B = _Voice("ta-IN", "ta-IN-Standard-B", Gender.MALE, 24000)
        TE_IN_STANDARD_A = _Voice("te-IN", "te-IN-Standard-A", Gender.FEMALE, 24000)
        TE_IN_STANDARD_B = _Voice("te-IN", "te-IN-Standard-B", Gender.MALE, 24000)
        TH_TH_STANDARD_A = _Voice("th-TH", "th-TH-Standard-A", Gender.FEMALE, 22050)
        TR_TR_STANDARD_A = _Voice("tr-TR", "tr-TR-Standard-A", Gender.FEMALE, 24000)
        TR_TR_STANDARD_B = _Voice("tr-TR", "tr-TR-Standard-B", Gender.MALE, 24000)
        TR_TR_STANDARD_C = _Voice("tr-TR", "tr-TR-Standard-C", Gender.FEMALE, 24000)
        TR_TR_STANDARD_D = _Voice("tr-TR", "tr-TR-Standard-D", Gender.FEMALE, 24000)
        TR_TR_STANDARD_E = _Voice("tr-TR", "tr-TR-Standard-E", Gender.MALE, 24000)
        UK_UA_STANDARD_A = _Voice("uk-UA", "uk-UA-Standard-A", Gender.FEMALE, 24000)
        VI_VN_STANDARD_A = _Voice("vi-VN", "vi-VN-Standard-A", Gender.FEMALE, 24000)
        VI_VN_STANDARD_B = _Voice("vi-VN", "vi-VN-Standard-B", Gender.MALE, 24000)
        VI_VN_STANDARD_C = _Voice("vi-VN", "vi-VN-Standard-C", Gender.FEMALE, 24000)
        VI_VN_STANDARD_D = _Voice("vi-VN", "vi-VN-Standard-D", Gender.MALE, 24000)
        YUE_HK_STANDARD_A = _Voice("yue-HK", "yue-HK-Standard-A", Gender.FEMALE, 24000)
        YUE_HK_STANDARD_B = _Voice("yue-HK", "yue-HK-Standard-B", Gender.MALE, 24000)
        YUE_HK_STANDARD_C = _Voice("yue-HK", "yue-HK-Standard-C", Gender.FEMALE, 24000)
        YUE_HK_STANDARD_D = _Voice("yue-HK", "yue-HK-Standard-D", Gender.MALE, 24000)

    class WaveNet:
        AR_XA_WAVENET_A = _Voice("ar-XA", "ar-XA-Wavenet-A", Gender.FEMALE, 24000)
        AR_XA_WAVENET_B = _Voice("ar-XA", "ar-XA-Wavenet-B", Gender.MALE, 24000)
        AR_XA_WAVENET_C = _Voice("ar-XA", "ar-XA-Wavenet-C", Gender.MALE, 24000)
        CMN_CN_WAVENET_A = _Voice("cmn-CN", "cmn-CN-Wavenet-A", Gender.FEMALE, 24000)
        CMN_CN_WAVENET_B = _Voice("cmn-CN", "cmn-CN-Wavenet-B", Gender.MALE, 24000)
        CMN_CN_WAVENET_C = _Voice("cmn-CN", "cmn-CN-Wavenet-C", Gender.MALE, 24000)
        CMN_CN_WAVENET_D = _Voice("cmn-CN", "cmn-CN-Wavenet-D", Gender.FEMALE, 24000)
        CMN_TW_WAVENET_A = _Voice("cmn-TW", "cmn-TW-Wavenet-A", Gender.FEMALE, 24000)
        CMN_TW_WAVENET_B = _Voice("cmn-TW", "cmn-TW-Wavenet-B", Gender.MALE, 24000)
        CMN_TW_WAVENET_C = _Voice("cmn-TW", "cmn-TW-Wavenet-C", Gender.MALE, 24000)
        CS_CZ_WAVENET_A = _Voice("cs-CZ", "cs-CZ-Wavenet-A", Gender.FEMALE, 24000)
        DA_DK_WAVENET_A = _Voice("da-DK", "da-DK-Wavenet-A", Gender.FEMALE, 24000)
        DA_DK_WAVENET_C = _Voice("da-DK", "da-DK-Wavenet-C", Gender.MALE, 24000)
        DA_DK_WAVENET_D = _Voice("da-DK", "da-DK-Wavenet-D", Gender.FEMALE, 24000)
        DA_DK_WAVENET_E = _Voice("da-DK", "da-DK-Wavenet-E", Gender.FEMALE, 24000)
        DE_DE_WAVENET_A = _Voice("de-DE", "de-DE-Wavenet-A", Gender.FEMALE, 24000)
        DE_DE_WAVENET_B = _Voice("de-DE", "de-DE-Wavenet-B", Gender.MALE, 24000)
        DE_DE_WAVENET_C = _Voice("de-DE", "de-DE-Wavenet-C", Gender.FEMALE, 24000)
        DE_DE_WAVENET_D = _Voice("de-DE", "de-DE-Wavenet-D", Gender.MALE, 24000)
        DE_DE_WAVENET_E = _Voice("de-DE", "de-DE-Wavenet-E", Gender.MALE, 24000)
        DE_DE_WAVENET_F = _Voice("de-DE", "de-DE-Wavenet-F", Gender.FEMALE, 24000)
        EL_GR_WAVENET_A = _Voice("el-GR", "el-GR-Wavenet-A", Gender.FEMALE, 24000)
        EN_AU_WAVENET_A = _Voice("en-AU", "en-AU-Wavenet-A", Gender.FEMALE, 24000)
        EN_AU_WAVENET_B = _Voice("en-AU", "en-AU-Wavenet-B", Gender.MALE, 24000)
        EN_AU_WAVENET_C = _Voice("en-AU", "en-AU-Wavenet-C", Gender.FEMALE, 24000)
        EN_AU_WAVENET_D = _Voice("en-AU", "en-AU-Wavenet-D", Gender.MALE, 24000)
        EN_GB_WAVENET_A = _Voice("en-GB", "en-GB-Wavenet-A", Gender.FEMALE, 24000)
        EN_GB_WAVENET_B = _Voice("en-GB", "en-GB-Wavenet-B", Gender.MALE, 24000)
        EN_GB_WAVENET_C = _Voice("en-GB", "en-GB-Wavenet-C", Gender.FEMALE, 24000)
        EN_GB_WAVENET_D = _Voice("en-GB", "en-GB-Wavenet-D", Gender.MALE, 24000)
        EN_GB_WAVENET_F = _Voice("en-GB", "en-GB-Wavenet-F", Gender.FEMALE, 24000)
        EN_IN_WAVENET_A = _Voice("en-IN", "en-IN-Wavenet-A", Gender.FEMALE, 24000)
        EN_IN_WAVENET_B = _Voice("en-IN", "en-IN-Wavenet-B", Gender.MALE, 24000)
        EN_IN_WAVENET_C = _Voice("en-IN", "en-IN-Wavenet-C", Gender.MALE, 24000)
        EN_IN_WAVENET_D = _Voice("en-IN", "en-IN-Wavenet-D", Gender.FEMALE, 24000)
        EN_US_WAVENET_A = _Voice("en-US", "en-US-Wavenet-A", Gender.MALE, 24000)
        EN_US_WAVENET_B = _Voice("en-US", "en-US-Wavenet-B", Gender.MALE, 24000)
        EN_US_WAVENET_C = _Voice("en-US", "en-US-Wavenet-C", Gender.FEMALE, 24000)
        EN_US_WAVENET_D = _Voice("en-US", "en-US-Wavenet-D", Gender.MALE, 24000)
        EN_US_WAVENET_E = _Voice("en-US", "en-US-Wavenet-E", Gender.FEMALE, 24000)
        EN_US_WAVENET_F = _Voice("en-US", "en-US-Wavenet-F", Gender.FEMALE, 24000)
        EN_US_WAVENET_G = _Voice("en-US", "en-US-Wavenet-G", Gender.FEMALE, 24000)
        EN_US_WAVENET_H = _Voice("en-US", "en-US-Wavenet-H", Gender.FEMALE, 24000)
        EN_US_WAVENET_I = _Voice("en-US", "en-US-Wavenet-I", Gender.MALE, 24000)
        EN_US_WAVENET_J = _Voice("en-US", "en-US-Wavenet-J", Gender.MALE, 24000)
        FIL_PH_WAVENET_A = _Voice("fil-PH", "fil-PH-Wavenet-A", Gender.FEMALE, 24000)
        FIL_PH_WAVENET_B = _Voice("fil-PH", "fil-PH-Wavenet-B", Gender.FEMALE, 24000)
        FIL_PH_WAVENET_C = _Voice("fil-PH", "fil-PH-Wavenet-C", Gender.MALE, 24000)
        FIL_PH_WAVENET_D = _Voice("fil-PH", "fil-PH-Wavenet-D", Gender.MALE, 24000)
        FI_FI_WAVENET_A = _Voice("fi-FI", "fi-FI-Wavenet-A", Gender.FEMALE, 24000)
        FR_CA_WAVENET_A = _Voice("fr-CA", "fr-CA-Wavenet-A", Gender.FEMALE, 24000)
        FR_CA_WAVENET_B = _Voice("fr-CA", "fr-CA-Wavenet-B", Gender.MALE, 24000)
        FR_CA_WAVENET_C = _Voice("fr-CA", "fr-CA-Wavenet-C", Gender.FEMALE, 24000)
        FR_CA_WAVENET_D = _Voice("fr-CA", "fr-CA-Wavenet-D", Gender.MALE, 24000)
        FR_FR_WAVENET_A = _Voice("fr-FR", "fr-FR-Wavenet-A", Gender.FEMALE, 24000)
        FR_FR_WAVENET_B = _Voice("fr-FR", "fr-FR-Wavenet-B", Gender.MALE, 24000)
        FR_FR_WAVENET_C = _Voice("fr-FR", "fr-FR-Wavenet-C", Gender.FEMALE, 24000)
        FR_FR_WAVENET_D = _Voice("fr-FR", "fr-FR-Wavenet-D", Gender.MALE, 24000)
        FR_FR_WAVENET_E = _Voice("fr-FR", "fr-FR-Wavenet-E", Gender.FEMALE, 24000)
        HI_IN_WAVENET_A = _Voice("hi-IN", "hi-IN-Wavenet-A", Gender.FEMALE, 24000)
        HI_IN_WAVENET_B = _Voice("hi-IN", "hi-IN-Wavenet-B", Gender.MALE, 24000)
        HI_IN_WAVENET_C = _Voice("hi-IN", "hi-IN-Wavenet-C", Gender.MALE, 24000)
        HI_IN_WAVENET_D = _Voice("hi-IN", "hi-IN-Wavenet-D", Gender.FEMALE, 24000)
        HU_HU_WAVENET_A = _Voice("hu-HU", "hu-HU-Wavenet-A", Gender.FEMALE, 24000)
        ID_ID_WAVENET_A = _Voice("id-ID", "id-ID-Wavenet-A", Gender.FEMALE, 24000)
        ID_ID_WAVENET_B = _Voice("id-ID", "id-ID-Wavenet-B", Gender.MALE, 24000)
        ID_ID_WAVENET_C = _Voice("id-ID", "id-ID-Wavenet-C", Gender.MALE, 24000)
        ID_ID_WAVENET_D = _Voice("id-ID", "id-ID-Wavenet-D", Gender.FEMALE, 24000)
        IT_IT_WAVENET_A = _Voice("it-IT", "it-IT-Wavenet-A", Gender.FEMALE, 24000)
        IT_IT_WAVENET_B = _Voice("it-IT", "it-IT-Wavenet-B", Gender.FEMALE, 24000)
        IT_IT_WAVENET_C = _Voice("it-IT", "it-IT-Wavenet-C", Gender.MALE, 24000)
        IT_IT_WAVENET_D = _Voice("it-IT", "it-IT-Wavenet-D", Gender.MALE, 24000)
        JA_JP_WAVENET_A = _Voice("ja-JP", "ja-JP-Wavenet-A", Gender.FEMALE, 24000)
        JA_JP_WAVENET_B = _Voice("ja-JP", "ja-JP-Wavenet-B", Gender.FEMALE, 24000)
        JA_JP_WAVENET_C = _Voice("ja-JP", "ja-JP-Wavenet-C", Gender.MALE, 24000)
        JA_JP_WAVENET_D = _Voice("ja-JP", "ja-JP-Wavenet-D", Gender.MALE, 24000)
        KO_KR_WAVENET_A = _Voice("ko-KR", "ko-KR-Wavenet-A", Gender.FEMALE, 24000)
        KO_KR_WAVENET_B = _Voice("ko-KR", "ko-KR-Wavenet-B", Gender.FEMALE, 24000)
        KO_KR_WAVENET_C = _Voice("ko-KR", "ko-KR-Wavenet-C", Gender.MALE, 24000)
        KO_KR_WAVENET_D = _Voice("ko-KR", "ko-KR-Wavenet-D", Gender.MALE, 24000)
        NB_NO_WAVENET_A = _Voice("nb-NO", "nb-NO-Wavenet-A", Gender.FEMALE, 24000)
        NB_NO_WAVENET_B = _Voice("nb-NO", "nb-NO-Wavenet-B", Gender.MALE, 24000)
        NB_NO_WAVENET_C = _Voice("nb-NO", "nb-NO-Wavenet-C", Gender.FEMALE, 24000)
        NB_NO_WAVENET_D = _Voice("nb-NO", "nb-NO-Wavenet-D", Gender.MALE, 24000)
        NB_NO_WAVENET_E = _Voice("nb-NO", "nb-no-Wavenet-E", Gender.FEMALE, 24000)
        NL_NL_WAVENET_A = _Voice("nl-NL", "nl-NL-Wavenet-A", Gender.FEMALE, 24000)
        NL_NL_WAVENET_B = _Voice("nl-NL", "nl-NL-Wavenet-B", Gender.MALE, 24000)
        NL_NL_WAVENET_C = _Voice("nl-NL", "nl-NL-Wavenet-C", Gender.MALE, 24000)
        NL_NL_WAVENET_D = _Voice("nl-NL", "nl-NL-Wavenet-D", Gender.FEMALE, 24000)
        NL_NL_WAVENET_E = _Voice("nl-NL", "nl-NL-Wavenet-E", Gender.FEMALE, 24000)
        PL_PL_WAVENET_A = _Voice("pl-PL", "pl-PL-Wavenet-A", Gender.FEMALE, 24000)
        PL_PL_WAVENET_B = _Voice("pl-PL", "pl-PL-Wavenet-B", Gender.MALE, 24000)
        PL_PL_WAVENET_C = _Voice("pl-PL", "pl-PL-Wavenet-C", Gender.MALE, 24000)
        PL_PL_WAVENET_D = _Voice("pl-PL", "pl-PL-Wavenet-D", Gender.FEMALE, 24000)
        PL_PL_WAVENET_E = _Voice("pl-PL", "pl-PL-Wavenet-E", Gender.FEMALE, 24000)
        PT_BR_WAVENET_A = _Voice("pt-BR", "pt-BR-Wavenet-A", Gender.FEMALE, 24000)
        PT_PT_WAVENET_A = _Voice("pt-PT", "pt-PT-Wavenet-A", Gender.FEMALE, 24000)
        PT_PT_WAVENET_B = _Voice("pt-PT", "pt-PT-Wavenet-B", Gender.MALE, 24000)
        PT_PT_WAVENET_C = _Voice("pt-PT", "pt-PT-Wavenet-C", Gender.MALE, 24000)
        PT_PT_WAVENET_D = _Voice("pt-PT", "pt-PT-Wavenet-D", Gender.FEMALE, 24000)
        RU_RU_WAVENET_A = _Voice("ru-RU", "ru-RU-Wavenet-A", Gender.FEMALE, 24000)
        RU_RU_WAVENET_B = _Voice("ru-RU", "ru-RU-Wavenet-B", Gender.MALE, 24000)
        RU_RU_WAVENET_C = _Voice("ru-RU", "ru-RU-Wavenet-C", Gender.FEMALE, 24000)
        RU_RU_WAVENET_D = _Voice("ru-RU", "ru-RU-Wavenet-D", Gender.MALE, 24000)
        RU_RU_WAVENET_E = _Voice("ru-RU", "ru-RU-Wavenet-E", Gender.FEMALE, 24000)
        SK_SK_WAVENET_A = _Voice("sk-SK", "sk-SK-Wavenet-A", Gender.FEMALE, 24000)
        SV_SE_WAVENET_A = _Voice("sv-SE", "sv-SE-Wavenet-A", Gender.FEMALE, 24000)
        TR_TR_WAVENET_A = _Voice("tr-TR", "tr-TR-Wavenet-A", Gender.FEMALE, 24000)
        TR_TR_WAVENET_B = _Voice("tr-TR", "tr-TR-Wavenet-B", Gender.MALE, 24000)
        TR_TR_WAVENET_C = _Voice("tr-TR", "tr-TR-Wavenet-C", Gender.FEMALE, 24000)
        TR_TR_WAVENET_D = _Voice("tr-TR", "tr-TR-Wavenet-D", Gender.FEMALE, 24000)
        TR_TR_WAVENET_E = _Voice("tr-TR", "tr-TR-Wavenet-E", Gender.MALE, 24000)
        UK_UA_WAVENET_A = _Voice("uk-UA", "uk-UA-Wavenet-A", Gender.FEMALE, 24000)
        VI_VN_WAVENET_A = _Voice("vi-VN", "vi-VN-Wavenet-A", Gender.FEMALE, 24000)
        VI_VN_WAVENET_B = _Voice("vi-VN", "vi-VN-Wavenet-B", Gender.MALE, 24000)
        VI_VN_WAVENET_C = _Voice("vi-VN", "vi-VN-Wavenet-C", Gender.FEMALE, 24000)
        VI_VN_WAVENET_D = _Voice("vi-VN", "vi-VN-Wavenet-D", Gender.MALE, 24000)

    # Female WaveNet default voice
    DEFAULT = WaveNet.EN_US_WAVENET_H


# Class variable generation for `Voices` class
# using Google Cloud API
def _generate_standard_voice_constants():
    voices = {
        _format_constant(voice)
        for voice in _all_voices()
        if "standard" in voice.name.lower()
    }
    return sorted(voices)


def _generate_wavenet_voice_constants():
    voices = {
        _format_constant(voice)
        for voice in _all_voices()
        if "wavenet" in voice.name.lower()
    }
    return sorted(voices)


def _all_voices():
    client = tts.TextToSpeechClient()
    response = client.list_voices()
    return response.voices


def _format_constant(voice):
    languages = ", ".join(voice.language_codes)
    name = voice.name
    gender = voice.ssml_gender
    rate = voice.natural_sample_rate_hertz

    member_name = "_".join(name.upper().split("-"))

    formatted = (
        f"{member_name} = {_Voice.__name__}('{languages}', "
        f"'{name}', Gender.{gender.name}, {rate})"
    )
    return formatted


def main():
    print(f"\tclass Standard:")
    for member in _generate_standard_voice_constants():
        print(f"\t\t{member}")
    print(f"\tclass WaveNet:")
    for member in _generate_wavenet_voice_constants():
        print(f"\t\t{member}")


if __name__ == "__main__":
    main()