using System;
using System.Threading;
using NetMQ;
using NetMQ.Sockets;
namespace Publisher
{
    class Program
    {
        static void Main(string[] args)
        {
            Random rand = new Random(50);
            using (var pubSocket = new PublisherSocket())
            {
                Console.WriteLine("Publisher socket binding...");
                pubSocket.Options.SendHighWatermark = 1000;
                pubSocket.Bind("tcp://127.0.0.1:5555"); // Sending to 127.0.0.1 port 5555
                for (var i = 0; i <10; i++)
                {
                    var msg = "msg-" + i;
                    Console.WriteLine("Sending message : {0}", msg);
                    pubSocket.SendMoreFrame("msg").SendFrame(msg); // Sending message use Topic "msg"
                    
                    Thread.Sleep(500);
                }

                string dir = "../../../../picture.jpg"; // Replace with the appropriate image path
                // Convert picture to byte array
                byte[] imageBytes = File.ReadAllBytes(dir);

                // Convert byte array to Base64 string
                string send_pic = Convert.ToBase64String(imageBytes);

                // Sending picture use Topic "img"
                Console.WriteLine("Sending picture from : {0}", dir);
                pubSocket.SendMoreFrame("img").SendFrame(send_pic);
            }
        }
    }
}