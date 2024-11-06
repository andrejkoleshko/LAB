1. echo "andrejkoleshko"
2. pwd > ~/otchet/files/2.txt && whoami >> ~/otchet/files/2.txt
3. ls -la ~/ > ~/otchet/files/3.txt
4. cat > ~/4.txt && cat ~/4.txt > ~/4.md
5. chmod go-r ~/4.txt
6. chmod 755 ~/4.md
7. mv ~/4.txt ~/otchet/files && mv ~/4.md ~/otchet/files
8. sudo chown root ~/otchet/files/4.md
9. sudo useradd -ms /bin/zsh test_user 
10. sudo passwd test_user
11. sudo usermod -aG wheel test_user
12. cat /etc/passwd > ~/otchet/files/12.txt
13. chmod a+w ~/otchet/files/12.txt
14. su -P test_user
15. whoami >> ~/otchet/files/12.txt && pwd >> ~/otchet/files/12.txt
16. 
17. sudo su
18. commands in punkt 15
19. tail -n 2 ~/otchet/files/12.txt
20. sudo userdel -r test_user 
21. find ~/ -maxdepth 2 -type d -empty > ~/otchet/files/21.txt
22. sudo find / -maxdepth 3 -name "*dev*" -user root > ~/otchet/files/22.txt
23. mkdir test_find && mkdir test_find/time && mkdir test_find/permissions
24. touch -ad "2024-01-01" test_find/time/one.txt && touch -md "2024-10-14" test_find/time/two.txt
25. touch test_find/permissions/cant_write.txt && touch test_find/permissions/can_execute.txt && chmod a-w test_find/permissions/cant_write.txt && chmod a+x test_find/permissions/can_execute.txt
26. find test_find/ -type f -empty -exec rm {} \;
27. find test_find/ -perm 755 -type f -empty -exec chmod a-x {} \;
28. man ls > man_ls.txt
29. grep -n "^$" man_ls.txt
30. grep "[0-9]" man_ls.txt
31. grep -w "Richard" man_ls.txt > ~/otchet/files/31.txt
32. wc -lc ~/otchet/files/31.txt
33. ps aux > ~/otchet/files/33.txt
34. 
35. ps -C nano
36. pkill -quit nano