// See https://aka.ms/new-console-template for more information
Console.WriteLine("Hello, World!");


const string dirname = "H:\\AIMG-362\\PDF_Reports_2213_final";
const string dirname2 = "H:\\AIMG-362\\PDF_Reports_2213_final(copy)\\";

if (!Directory.Exists(dirname2)){ Directory.CreateDirectory(dirname2);}



Array fileList = Directory.GetFiles(dirname);

foreach (String path in fileList) {
    FileInfo fi = new FileInfo(path);
    if (File.Exists(path)) {
        //Console.WriteLine(dirname2 + fi.Name);
        File.Move(path,dirname2 + fi.Name);
    };
}
