from m05_my_lab_util import read_file, print_profiles, show_profile

profile_path = r"c:\tmp\m04_lab_profiles.txt"

profile_dict = dict()
sorted_list = list()


profile_dict = read_file(profile_path)

sorted_list = []
for name, profile in profile_dict.items():
    sorted_list.append([name, profile])
print_profiles("  Unsorted List   ", sorted_list)

# sorting of dictionary of dictionaries
sorted_list = list(sorted(profile_dict.items(),
                          key=lambda k_v: k_v[1]["name"]))
print_profiles("  Sorted by Name  ", sorted_list)

sorted_list = list(sorted(profile_dict.items(),
                          key=lambda k_v: k_v[1]["location"]))
print_profiles("Sorted by Location", sorted_list)

sorted_list = list(sorted(profile_dict.items(),
                          key=lambda k_v: k_v[1]["employer"]))
print_profiles("Sorted by Employer", sorted_list)

while True:
    name_to_find = input("\nEnter name: ")
    if len(name_to_find) == 0:
        break

    show_profile(name_to_find, profile_dict)
