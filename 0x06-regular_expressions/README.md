# 0x06. Regular expression

For this project, you have to build your regular expression using Oniguruma, a regular expression library that which is used by Ruby by default. Note that other regular expression libraries sometimes have different properties.

Because the focus of this exercise is to play with regular expressions (regex), here is the Ruby code that you should use, just replace the regexp part, meaning the code in between the //:

```
sylvain@ubuntu$ cat example.rb
#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join
sylvain@ubuntu$
sylvain@ubuntu$ ./example.rb 127.0.0.2
127.0.0.2
sylvain@ubuntu$ ./example.rb 127.0.0.1
127.0.0.1
sylvain@ubuntu$ ./example.rb 127.0.0.a
```

## Requirements

- Allowed editors: vi, vim, emacs
- All your files will be interpreted on Ubuntu 14.04 LTS
- All your files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- The first line of all your Bash scripts should be exactly #!/usr/bin/env ruby
- All your regex must be built for the Oniguruma library

## About Holberton

<p>
<img height="150" src="https://blog.holbertonschool.com/wp-content/uploads/2020/04/unnamed-2.png" align="right" >
</p>

Holberton teaches full-stack software engineering with a project-based approach.
The first part of our on-site intensive education covers the foundations of software
engineering, including low-level programming, DevOps, and high-level modern languages.

This project is part of *system engineering and devops*, where you will build web infrastructure similar to those powering tech powerhouses like LinkedIn,
Facebook, and Google. You will architect scalable, reliable, and secure systems using web
servers, load balancers, databases, firewalls, and more. You will learn to automate your job
so that you can easily manage anything from one server or hundreds of them.
