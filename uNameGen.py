import argparse

def banner():
    txt = f"""

        _   _                       ____            
  _   _| \ | | __ _ _ __ ___   ___ / ___| ___ _ __  
 | | | |  \| |/ _` | '_ ` _ \ / _ \ |  _ / _ \ '_ \ 
 | |_| | |\  | (_| | | | | | |  __/ |_| |  __/ | | |
  \__,_|_| \_|\__,_|_| |_| |_|\___|\____|\___|_| |_|
  
  by @AnxxJan
                                                    
                   """
    print(txt)

def process_names(file_name, verbose=False):
    names_dict = {}
    try:
        with open(file_name, 'r') as file:
            for line in file:
                first_name, last_name = line.strip().split()
                username = first_name[0].lower() + last_name.lower()
                camelcase_name = first_name.capitalize() + last_name.capitalize()
                full_name = first_name
                names_dict[username] = [camelcase_name, full_name]
                if verbose:
                    print("Username:", username)
                    print("CamelCase:", camelcase_name)
                    print("Full Name:", full_name)
                    print()
        return names_dict
    except FileNotFoundError:
        print("The specified file was not found.")
    except Exception as e:
        print("An error occurred:", e)

def save_names(names_dict, output_file):
    try:
        with open(output_file, 'w') as file:
            for username, details in names_dict.items():
                file.write(username + '\n')
                file.write(details[0] + '\n')
                file.write(details[1] + '\n')
        print("★ Names successfully saved to", output_file, "★")
    except Exception as e:
        print("An error occurred while saving names:", e)

def main():
    parser = argparse.ArgumentParser(description="Process names from a text file and save them.")
    parser.add_argument('-n', '--file_name', type=str, required=True, help='Path of the text file')
    parser.add_argument('-o', '--output_file', type=str, default='wordlist.txt', help='Output file name')
    parser.add_argument('-v', '--verbose', action='store_true', help='Display generated names in console')
    args = parser.parse_args()

    names_dict = process_names(args.file_name, args.verbose)
    if names_dict:
        save_names(names_dict, args.output_file)

if __name__ == "__main__":
    banner()
    main()
