from django.http import HttpResponse
from backend.util import generate_opcode_csv, generate_opcode_tree
from opcode_django.settings import BASE_DIR
import json


def test(request):
    result = {'data': 'A'}
    return HttpResponse(json.dumps(result), content_type='application/json')


# 根据aliuid获取uuid
def get_opcode_uuid(request):
    params = json.loads(request.body)
    params_aliuid = params['aliuid']
    # params_aliuid = '2649ab00c2a10567448a45fd6ec09add'

    with open(str(BASE_DIR) + '/backend/data/opcode_uuid.json', 'r', encoding='utf8') as fp:
        json_data = json.load(fp)

    origin_result = json_data[params_aliuid]
    result = []
    for o in origin_result:
        result.append(o)

    return HttpResponse(json.dumps(result), content_type='application/json')


# 根据aliuid，uuid获取file_md5
def get_opcode_file_md5(request):
    params = json.loads(request.body)
    params_aliuid = params['aliuid']
    params_uuid = params['uuid']

    # params_aliuid = '2649ab00c2a10567448a45fd6ec09add'
    # params_uuid = 'a889f5ee466a326539356f938502f1a2'

    with open(str(BASE_DIR) + '/backend/data/opcode_file_md5.json', 'r', encoding='utf8') as fp:
        json_data = json.load(fp)

    akey = params_aliuid + '|' + params_uuid
    origin_result = json_data[akey]
    result = []
    for o in origin_result:
        result.append(o)

    return HttpResponse(json.dumps(result), content_type='application/json')


# 根据aliuid，uuid，file_MD5获取tree_map
def get_opcode_tree_map(request):
    params = json.loads(request.body)
    params_aliuid = params['aliuid']
    params_uuid = params['uuid']
    params_file_md5 = params['file_md5']
    tree_type = params['tree_type']   # 分为all_point stain

    # params_aliuid = '2649ab00c2a10567448a45fd6ec09add'
    # params_uuid = 'a889f5ee466a326539356f938502f1a2'
    # params_file_md5 = '899e763467eba8a2a340c975b7de1d02'
    # tree_type = 'all_point'
    opcode_csv = generate_opcode_csv(params_aliuid, params_uuid, params_file_md5)
    opcode_tree = generate_opcode_tree(opcode_csv, tree_type)

    return HttpResponse(json.dumps(opcode_tree[0]), content_type='application/json')

