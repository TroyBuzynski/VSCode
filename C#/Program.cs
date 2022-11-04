// See https://aka.ms/new-console-template for more information
using MailKit.Net.Smtp;
using MailKit;
using MimeKit;


MimeMessage message = new MimeMessage();
message.From.Add(new MailboxAddress("Tester", "buz8658@gmail.com" ));

message.To.Add(MailboxAddress.Parse("troy.buzynski@uni.edu"));

message.Subject = "Fail";

message.Body = new TextPart("plain"){
    Text = @"Yes,
    DHellow!
    This is a Dog!"
};

string emailAddress = "buz8658@gmail.com";

string password = "jyffEg-5qatce-kacsuv";

SmtpClient client = new SmtpClient();

try
{
    client.Connect("smtp.gmail.com", 645,true);
    client.Authenticate(emailAddress,password);
    client.Send(message);

    Console.WriteLine("Email Sent!");
}
catch (System.Exception e)
{
    Console.WriteLine(e.Message);
    throw;
}
finally{
    client.Disconnect(true);
    client.Dispose();
    //some changes
}