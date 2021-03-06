from elasticsearch import Elasticsearch as client_elastic
import os

LOCAL_HOST_NAME = "http://localhost"
LOCAL_PORT = "9200"

SERVER_HOST_NAME = "http://54.68.196.78"
SERVER_PORT = "9200"
SERVER_AUTH_USER = "elastic"
SERVER_AUTH_PASS = "elasticbk"

# directory path
system_config = "system_config.json"
pipeline_config = "pipeline_config.json"


# call local or server elastic search

def local_elastic():
    return client_elastic(hosts=[LOCAL_HOST_NAME], port=LOCAL_PORT, timeout=90)


def server_elastic():
    return client_elastic(hosts=[SERVER_HOST_NAME],
                          http_auth=(SERVER_AUTH_USER, SERVER_AUTH_PASS),
                          port=SERVER_PORT, timeout=90)


def create_client_elastic_search(type):
    if type == LOCAL_HOST_NAME:
        return local_elastic()
    elif type == SERVER_HOST_NAME:
        return server_elastic()
    else:
        return None


# pattern for each key tag
pattern_search = {
    "Salary": [
        "lương (.*?) (((\d{1,}.)?)+\d{3,}.\d{3,}(-((\d{1,}.)?)+\d{3,}.\d{3,})?)",
        "lương (.*?) (\d{1,}) triệu đồng",
        "lương (.*?) (\d{1,})",
        "lương",
        "mức đãi ngộ",
        "thu nhập",
        "lương cao",
        "chính sách lương",
        "mức lương",
    ],
    "Environment": [
        "môi trường làm việc",
        "chất lượng môi trường",
        "đào tạo nguồn nhân lực",
        "đào tạo và hỗ trợ nhân sự",
        "văn hóa doanh nghiệp",
        "cơ sở hạ tầng",
        "môi trường công tác",
        "văn hóa tổ chức",
        "trang thiết bị hiện đại",
        "học hỏi công nghệ mới",
        "hỗ trợ thực tập",
        "hỗ trợ nhân viên"
    ],
    "Regime": [
        "chính sách thu hút",
        "chính sách đối với người có tài năng",
        "chính sách trọng dụng",
        "chính sách trọng dụng nhân tài",
        "chế độ",
        "chính sách lựa chọn",
        "chính sách thí điểm thu hút",
        "chính sách khuyến khích",
        "cơ chế,"
    ]
}
pattern_key = {
    "Salary":
        [
            "lương",
            "mức đãi ngộ",
            "đãi ngộ",
            "thu nhập",
        ],
    "Environment":
        [
            "môi trường làm việc",
            "đào tạo nguồn nhân lực",
            "đào tạo và hỗ trợ nhân sự",
            "văn hóa doanh nghiệp",
            "cơ sở hạ tầng",
            "môi trường công tác",
            "văn hóa tổ chức",
            "đào tạo sinh viên trẻ",
            "trang thiết bị hiện đại",
            "học hỏi công nghệ mới",
            "hỗ trợ thực tập",
            "hỗ trợ nhân viên"
        ],
    "Regime":
        [
            "chính sách",
            "chế độ",
            "cơ chế"
        ]
}

# index of elastic search server
talent_crawled_index = "talent-crawled"
talent_cleaned_index = "talent-cleaned"
