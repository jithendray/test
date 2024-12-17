---
layout: post
title: EndeavourOS is amazing!
description: I've been using EndeavourOS as my daily driver for about a year now, and I absolutely love it. I want to write about how I found EndeavourOS, why I decided to move to it, and what’s keeping me here for so long. Let's dive deep?
tags:
  - linux
  - arch
  - endeavouros
---
I'm a total distro hopper and have this funny goal of trying out every Linux distro out there (well, at least as many as I can!). Over the last six years, I’ve used a bunch of them—started with Ubuntu (obviously), then went through Linux Mint, Lubuntu, Kubuntu, Pop!OS, Manjaro, and now I’m on EndeavourOS.

I've been using EndeavourOS exclusively for the past year, and I must admit that I'm really enjoying it. I don't usually stick with one distribution for very long, but this one just seemed right, and I don't have any plans to swap anytime soon. I want to write about how I found EndeavourOS, why I decided to move to it, and what’s keeping me here for so long.

### The Issue with Ubuntu/Debian based distros

Ubuntu is where almost everyone, including myself, begins their Linux adventure. Why not? It is user-friendly, incredibly simple to install, stable, and free of unexpected malfunctions. Plus, almost every software on these distros works perfectly and rarely breaks.

![]({{ site.baseurl }}/images/posts/2024-09-22/debian-ubuntu.jpg "debian-ubuntu")

So, why did I switch?

I'm not against ubuntu or debian-based distros. They’re solid and reliable. But for me, there were two reasons:
- **Distro hopping** – As I mentioned earlier, I enjoy exploring and trying out new Linux distributions.
- **More freedom** – Linux itself means freedom, But I wanted to experiment with a distro that gives me complete control. 

And that’s Arch!

### Why I installed Manjaro over Arch

Back then, I wasn’t really in the mood to go through Arch’s manual installation process. I wanted something fast and was too excited to try a new distro, even though I know it would have been enjoyable. While hunting for the perfect distro, I came across this badass [MANJARO](https://manjaro.org/).

![]({{ site.baseurl }}/images/posts/2024-09-22/manjaro.png "manjaro")


Manjaro is based on Arch but offers a lot more smoother onboarding process, particularly for beginners like myself (back then). It kept all the core strengths of Arch while making things simpler and more beginner-friendly. The installation process was super straightforward - compared to Arch’s more technical and time-consuming setup (or at least that’s what I had heard back then).

### Falling in LOVE with ARCH

I simply fell in love with Arch when I was using Manjaro. I was able to configure my system and fine-tune every single aspect of my environment. 

I always had access to the most recent software versions because Arch and Arch-based distributions release updates very often, in contrast to Debian's stable release model. Of course, the trade-off is that some software might occasionally break since Arch gets updates before they’re fully tested—but, that’s part of the thrill for me LOL!

Arch's documentation is what really makes it unique. With organized instructions for installation, troubleshooting, and everything in between, the [Arch Wiki](https://wiki.archlinux.org/) is far superior to the documentation for other distributions.

![]({{ site.baseurl }}/images/posts/2024-09-22/arch.jpg "arch")

And then there’s [pacman](https://wiki.archlinux.org/title/Pacman), Arch’s package manager. After using pacman, I can’t imagine going back to Debian’s apt or even yum. They’re painfully slow compared to pacman—I mean, it took apt 15 minutes to install Waterfox on my laptop, while pacman installed it in just 1 minute on the same machine!

But the real MVP for me is the [Arch User Repository (AUR)](https://aur.archlinux.org/). A huge selection of software packages that are not available in the official repositories can be found in this community-maintained repository. It's similar like having access to an endless supply of Linux apps!

### Why was I on distro hunt again?

I mean, I was pretty happy with Manjaro. But after using it for a few months and learning more about Arch, I realized something: **Manjaro isn’t pure Arch**.  On top of Arch, it adds numerous layers of customisation with changes and command-line tools exclusive to Manjaro. I began to feel a little bloated after a time.

And then there was _that_ incident—Manjaro completely killed itself during an update. I wasn’t expecting that at all.

That’s when I decided I needed something closer to pure Arch, with less custom packaging and a more efficient approach to managing software while still having a user-friendly onboarding process compared to directly installing Arch.

### Spotlight: EndeavourOS

EndeavourOS is another Arch-based distribution, and its primary goal is to stay as close to Arch as possible. Unlike Manjaro, which uses its own Calamares installer, EndeavourOS offers a more hands-on installation process. It does provide an installer, but it's optional and permits more customization during setup.

EndeavourOS is essentially bare-bones Arch, giving users the freedom to choose their preferred desktop environment. It doesn’t come preloaded with the fine-tuned tweaks and additional tools that Manjaro offers, which worked great for me and it let me experiment with different desktop environments like i3wm, XFCE, KDE, and GNOME.

![]({{ site.baseurl }}/images/posts/2024-09-22/endeavouros.png "endeavouros")


On my 7-year-old laptop, EndeavourOS felt significantly faster and had greater system performance than Manjaro. On my 7-year-old laptop, EndeavourOS felt significantly faster and had greater system performance than Manjaro. EndeavourOS provides a more cutting-edge experience and releases packages far more quickly than Manjaro.

### Downloading and installing EndeavourOS

The first thing I noticed about EndeavourOS’s ISO files was that there weren’t separate download links for specific desktop flavors. I was a little confused - coming from the Debian and Manjaro, I was used to picking a pre-configured flavor like KDE Plasma. But then I discovered something that instantly made my day: **EndeavourOS lets you choose your desktop environment during the installation process!**

Knowing that I just needed one ISO file to install and test every flavor, I went ahead and downloaded the most recent version of the operating system. I proceeded to install KDE Plasma on EndeavourOS and began testing it. For someone like me, who is constantly on a hopping spree, this level of freedom was just perfect. What more could I ask for?

### Why I fell in LOVE with EndeavourOS

EndeavourOS is a user-friendly Arch-based distro with zero bloat, and that’s what hooked me. But it’s not just the distro - it’s the community. The EndeavourOS forums are hands down my favorite Linux community. Every time I log in, I see people actively discussing, solving issues together, and sharing knowledge. It’s not just helpful; it’s welcoming.

Another highlight? The amazing default and community-contributed wallpapers. Small detail, but they add so much personality to the distro!

![]({{ site.baseurl }}/images/posts/2024-09-22/endwal1.png "end-wal-1")

![]({{ site.baseurl }}/images/posts/2024-09-22/endwal2.jpeg "end-wal-2")

![]({{ site.baseurl }}/images/posts/2024-09-22/endwal3.webp "end-wal-3")

Currently, I am using both KDE and Debian and I love how easily I can switch desktop environments right from the lock screen.

And package managers—Manjaro’s Pamac just felt useless on EOS. Instead, EndeavourOS allowed me to continue using pacman and yay, which are ofcourse awesome. It’s the perfect balance between “everything just works” and “I can break stuff if I want to, yay!”

Finally, EndeavourOS feels like the sweet spot. It’s like Manjaro but without the unnecessary security layers and broken AUR dependencies. It’s like Arch, but I don’t have to bury myself in the wiki for hours (unless I want to). And the best part? I can still proudly say, “**I use ARCH, btw!**” 😎

![]({{ site.baseurl }}/images/posts/2024-09-22/usearch.jpg "btw-i-use-arch")

### Who should use EndeavourOS?

EndeavourOS is a wonderful choice for anyone who want to learn more about GNU/Linux. It follows the Arch philosophy, sproviding a clean installation procedure and an easy-to-use system while allowing for more customization. 

The community is smaller, but it is quite active and helpful, and a lot of the support is user-centric, so one’ll be engaging with the Arch way of doing things. This distribution is for those who are eager to learn, keep their systems up to date, and occasionally do manual interventions. 

If you’re considering EndeavourOS or any Arch-based distro like Manjaro, you'll need to commit yourself to continuously  monitoring forums, troubleshooting on your own, and being comfortable chatting with random people for advice and fixes.

One important thing to remember is that **Linux is different from Windows**. Distros such as Linux Mint or Ubuntu make things extremely simple, which is fantastic for beginners but leads to some users viewing Linux solely as a replacement for Windows. If you have that mindset, you’ll probably struggle with Arch or Arch-based distros like EndeavourOS. To enjoy these distros, you need to approach Linux with a more open and leaner mindset.

![]({{ site.baseurl }}/images/posts/2024-09-22/lvswvsm.jpg "linux-vs-windows-vs-mac")


 