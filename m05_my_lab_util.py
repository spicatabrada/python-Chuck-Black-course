def read_file(profile_path):
    profile_file = open(profile_path)
    profile_dict = dict()
    for profile in profile_file:
        user_profile = dict()
        line_item = profile.strip().split(",")
        user_profile["name"] = line_item[0]
        user_profile["location"] = line_item[1]
        user_profile["status"] = line_item[2]
        user_profile["employer"] = line_item[3]
        user_profile["job"] = line_item[4]
        profile_dict[user_profile["name"].lower()] = user_profile
    profile_file.close()
    return profile_dict


def print_profiles(title, sorted_list):
    print("")
    print(
        f"============================= {title} ========================================")
    print("Name              Location          Status    Employer              Job")
    print("----------------  ----------------  --------  --------------------  -------------")

    print_body(sorted_list)


def print_body(sorted_list):
    for profile in sorted_list:
        prof_dict = dict(profile[1])
        print("{:16}  {:16}  {:8}  {:21}  {:15}".format(
            prof_dict["name"],
            prof_dict["location"],
            prof_dict["status"],
            prof_dict["employer"],
            prof_dict["job"])
        )


def show_profile(name_to_find, profile_dict):
    normalized_name = name_to_find.lower()

    if normalized_name not in profile_dict:
        print(f"Profile '{name_to_find}' doesn't exist.")
    else:
        print("Result:      name: {}".format(
            profile_dict[normalized_name]["name"]))
        print("         location: {}".format(
            profile_dict[normalized_name]["location"]))
        print("           status: {}".format(
            profile_dict[normalized_name]["status"]))
        print("         employer: {}".format(
            profile_dict[normalized_name]["employer"]))
        print("              job: {}".format(
            profile_dict[normalized_name]["job"]))
