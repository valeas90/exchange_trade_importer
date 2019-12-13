def is_dict_valid(parsed_dict, fields_to_check):
    if len(parsed_dict) < len(fields_to_check):
        return False

    return all([e in parsed_dict for e in fields_to_check])
