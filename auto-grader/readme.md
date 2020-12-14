### How to deploy the test files

#### Mac OS

#### Apache

Start the apache:

```
sudo apachectl start
```

Create a file named "Sites" at the user's root folder.

Then creat a file ```/etc/apache2/users/yourusername.conf``` with the following contents:

```
<Directory "/Users/yourusername/Sites/">
Options Indexes MultiViews
AllowOverride None
Order allow,deny
Allow from all
</Directory>
```

Afterwards, comment the following content in the ```/etc/apache2/http.conf```.

![截屏2020-12-13 上午3.32.21](/Users/cuigang/Desktop/截屏2020-12-13 上午3.32.21.png)

One thing should be noticed is this line may be different. So I put a screenshot here rather than real code.

Then, comment the following content in the ```/etc/apache2/extra/httpd-userdir.conf```

```
Include /private/etc/apache2/users/*.conf
```

Now, run `sudo chown root:wheel /etc/apache2/users/yourusername.conf` and restart Apache.

#### Run the test file

To remain general, I put a sample test code in the final code files. Now we can simply put it in the ```Sites``` folder and run ```localhost``` to see it.

#### Upload the selenium test file

