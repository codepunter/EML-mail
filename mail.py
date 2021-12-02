def create_eml_file(configur, receiver_em, sender_list, html, output_file_path):

    message = MIMEMultipart('alternative')
    message["Subject"] = configur.get('Mail', 'Subject')
    message["From"] = "GM.GS.Research@accenture.com"
    message["To"] = ', '.join(sender_list)
    message.add_header("X-Unsent", "1")

    e_body = MIMEText(html, "html")  # Change
    message.attach(e_body)

    # add attachment
    # for f in [output_file_path]:
    #     with open(f, "rb") as fil:
    #         part = MIMEApplication(
    #             fil.read(),
    #             Name=basename(f)
    #         )
    #     # After the file is closed
    #     part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
    #     message.attach(part)
    head, tail = os.path.split(output_file_path)
    outfile_name = os.path.join(dir_path, "temp", os.path.splitext(tail)[0] + ".eml")
    with open(outfile_name, 'w') as outfile:
        gen = generator.Generator(outfile)
        gen.flatten(message)
    return outfile_name
