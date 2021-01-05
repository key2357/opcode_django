import MySQLdb
import json

db = MySQLdb.connect("localhost", "root", "password", "vcs_v2", charset='utf8')


def generate_uuid():
    cursor = db.cursor()
    cursor.execute("select aliuid, uuid from malware_op_code")
    desc = cursor.description
    all_data = cursor.fetchall()
    opcode_aliuid = [dict(zip([col[0] for col in desc], row)) for row in all_data]

    result = {}
    for oa in opcode_aliuid:
        if oa['aliuid'] not in result:
            result[oa['aliuid']] = {oa['uuid']: 0}
        else:
            if oa['uuid'] not in result[oa['aliuid']]:
                result[oa['aliuid']][oa['uuid']] = 0

    json_data = json.dumps(result)
    file_object = open('./backend/data/opcode_uuid.json', 'w')
    file_object.write(json_data)
    file_object.close()


def generate_file_md5():
    cursor = db.cursor()
    cursor.execute("select aliuid, uuid, file_md5 from malware_op_code")
    desc = cursor.description
    all_data = cursor.fetchall()
    opcode_file_md5 = [dict(zip([col[0] for col in desc], row)) for row in all_data]

    result = {}
    for oa in opcode_file_md5:
        okey = oa['aliuid'] + '|' + oa['uuid']

        if okey not in result:
            result[okey] = {oa['file_md5']: 0}
        else:
            if oa['file_md5'] not in result[okey]:
                result[okey][oa['file_md5']] = 0

    json_data = json.dumps(result)
    file_object = open('./backend/data/opcode_file_md5.json', 'w')
    file_object.write(json_data)
    file_object.close()


generate_file_md5()
