import boto3

def get_profiles_from_file(file_path):    
    profiles = []
    # Creates a list with file lines
    with open(file_path) as file:
        lines = file.readlines()
    # Remove special characters and new line character
    for line in lines:
        if line.startswith('['):
            profile = line.replace('[', '').replace(']', '').strip()
            if profile != "default":
                profiles.append(profile)
    return profiles

def get_certs_arn_list(client):
    certs_arn_list = []
    certs = client.list_certificates()['CertificateSummaryList']
    for item in certs:
        certs_arn_list.append(item['CertificateArn'])
    # print(certs_arn_list)
    return certs_arn_list

def describe_certificate(client, arn):
    try:
        response = client.describe_certificate(
            CertificateArn=arn
        )
        return response
    except:
        pass

credential_file_path = "SEU DIRETÓRIO do credentials"
profiles = get_profiles_from_file(credential_file_path)

for profile in profiles:
    session = boto3.Session(profile_name=profile)
    client = session.client("acm", region_name="sa-east-1")
    for cert_arn in get_certs_arn_list(client):
        try:
            print("{")
            print("\"Dominio\": ","\"",describe_certificate(client, cert_arn)['Certificate']['DomainValidationOptions'][0]['DomainName'],"\",")
            #print("Status: ",describe_certificate(client, cert_arn)['Certificate']['DomainValidationOptions'][0]['ValidationStatus'])
            print("\"Metodo\": ","\"",describe_certificate(client, cert_arn)['Certificate']['DomainValidationOptions'][0]['ValidationMethod'],"\",")
            print("\"Status\": ","\"",describe_certificate(client, cert_arn)['Certificate']['Status'],"\",")
            print("\"Validade\": ","\"",describe_certificate(client, cert_arn)['Certificate']['NotAfter'],"\"")
            print("}")
        except:
            print("\"Renovacao\": ","\"",describe_certificate(client, cert_arn)['Certificate']['RenewalEligibility'],"\"")
            print("}")
