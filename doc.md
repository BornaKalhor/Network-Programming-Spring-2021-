# **Network Programming Project**

In this project we’re going to implement or use some of the networking tools and get familiar with them.

For implementing the project I’m going to use Python 3🐍. Why? because Python is the most efficient programming language for automation therefore it’s extremely practical and suitable for this project.

Not to mention its handy libraries.

Now, before we proceed any further let’s take a look at some of the networking expressions we use in this project.

## **Packet Analyzing**

So, what is packet analyzing? When data is transmitted over network it does this by breaking into smaller chunks, these chunks are called ‘**packets’**. These packets travel from the source node to the destination node by passing through routers, switches, etc.

Using packet analyzer programs, we analyze the whole or part of this route to gain some information about the transmission. For instance we can analyze the transmission to see if any data breech or alternation has occurred. Or if the data has been transmitted properly. Or if it’s not transmitted properly, we can dig the problem. Seeing which router failed to do its job and fix it.

On wireless networks, this is a lot easier since you don’t need extra hardware. But in wired networks such as some of the local area networks it’s a little bit trickier because you need to have access to the switches, routers, etc.

## **Packet Sniffing**

The term ‘Sniffing’ got its name from an actual packet analyzer program called ‘Sniffer™’ which was widely used in the older times. So sniffing is analyzing in a sort.

But when we are using the term ‘sniffing’, we mean exactly what its name implies.

We intend to get access to the actual data being transferred on the network from one point to another and decode it if need be.

![packets sniffed and decoded](https://upload.wikimedia.org/wikipedia/commons/9/94/Wireshark_Example_Decode.png)

We may intentionally do this for penetration testing purposes or to see how vulnerable our network is to eavesdropping.

Now, back to our project…

For this project I’m going to use Wireshark(and the softwares that come with it like TShark), which is a free and open-source packet analyzer program available for everybody at Wireshark.org
![Wireshark](https://www.wireshark.org/docs/wsug_html_chunked/wsug_graphics/ws-time-reference.png)

Additionally, I’m going to use Pyshark library, which is a Python library used for data sniffing over a network and modules like socket, struct and etc.

## References
[Wireshark Website](wireshark.org)
[Wireshark on GitHub](https://github.com/wireshark/wireshark)
[Wikipedia](https://en.wikipedia.org/wiki/Packet_analyzer)
