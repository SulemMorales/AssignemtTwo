# Sulem Morales - ISS 212 - Assignment 2
# Resources referenced: Jenn Moody screenshot from assignment and assignment 2 walkthrough video
# I have not coded in very long, apologies in advance

def read_log(file_path):
    # I hope this works 3rd times the charm! This should open and read the log file
    with open(file_path, 'r') as file:
        return file.readlines()

def filter_threats(log_lines):
    #this should filter for suspicious entires
    suspicious_entries = []
    for line in log_lines:
        if "Failed root login" in line or "Failed Login Attempt" in line or "Suspicious activity" in line:
            suspicious_entries.append(line)
    return suspicious_entries # This will move the return statement outside of the for loop

def display_results(threats):
    #i hope this displays the suspicious entries found
    for threat in threats:
        print(threat)

if __name__ == '__main__':
    log_file = "access.log"
    log_data = read_log(log_file)
    threats = filter_threats(log_data)
    display_results(threats)