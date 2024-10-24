2. tree -d -L 2
3. cd /etc/
4. ls -a
5. ls -la / | sort -k 2
6. mkdir structure 
7. cd structure/     &&      mkdir -p {2018..2023}     &&      cd 2018/     &&      mkdir files pictures .passwords    &&       cd ../    &&       cd 2019/     &&      mkdir files pictures .passwords     &&      cd ../    &&       cd 2020/     &&      
   mkdir files pictures .passwords     &&      cd ../    &&       cd 2021/   &&        mkdir files pictures .passwords    &&       cd ../   &&        cd 2022/    &&       mkdir files pictures .passwords   &&        cd ../   &&        cd 2023/   &&       
   mkdir files pictures .passwords      &&     cd ~/
8. cd structure/2018/files/      &&     touch data.md    &&       cd ~/    &&       cd structure/2019/files/    &&       touch data.md    &&       cd ~/      &&     
   cd structure/2020/files/      &&     touch data.md    &&       cd ~/    &&       cd structure/2021/files/    &&       touch data.md    &&       cd ~/      &&     
   cd structure/2022/files/      &&     touch data.md    &&       cd ~/    &&       cd structure/2023/files/    &&       touch data.md    &&       cd ~/
9. cd structure/2018/pictures/      &&     touch picture.png    &&       cd ~/    &&       cd structure/2019/pictures/    &&       touch picture.png    &&       cd ~/      &&     
   cd structure/2020/pictures/      &&     touch picture.png    &&       cd ~/    &&       cd structure/2021/pictures/    &&       touch picture.png    &&       cd ~/      &&     
   cd structure/2022/pictures/      &&     touch picture.png    &&       cd ~/    &&       cd structure/2023/pictures/    &&       touch picture.png    &&       cd ~/ 
10. cd structure/2018/.passwords/      &&     touch .passwords.txt    &&       cd ~/    &&       cd structure/2019/.passwords/    &&       touch .passwords.txt    &&       cd ~/      &&     
    cd structure/2020/.passwords/      &&     touch .passwords.txt    &&       cd ~/    &&       cd structure/2021/.passwords/    &&       touch .passwords.txt    &&       cd ~/      &&     
    cd structure/2022/.passwords/      &&     touch .passwords.txt    &&       cd ~/    &&       cd structure/2023/.passwords/    &&       touch .passwords.txt    &&       cd ~/ 
11. touch -mad "2024-01-01" structure/2018/files/data.md      &&     touch -mad "2024-01-01" structure/2019/files/data.md      &&     
    touch -mad "2024-01-01" structure/2020/files/data.md      &&     touch -mad "2024-01-01" structure/2021/files/data.md      &&      
    touch -mad "2024-01-01" structure/2022/files/data.md      &&     touch -mad "2024-01-01" structure/2023/files/data.md
12. touch -mad "2018-06-10" structure/2018/.passwords/.passwords.txt      &&     touch -mad "2019-06-10" structure/2019/.passwords/.passwords.txt      &&     
    touch -mad "2020-06-10" structure/2020/.passwords/.passwords.txt      &&     touch -mad "2021-06-10" structure/2021/.passwords/.passwords.txt      &&      
    touch -mad "2022-06-10" structure/2022/.passwords/.passwords.txt      &&     touch -mad "2023-06-10" structure/2023/.passwords/.passwords.txt 
13. cp -R ~/structure/2023 ~/Downloads/2025
14. touch -mad "2025-06-10" Downloads/2025/.passwords/.passwords.txt
15. cp -R ~/Downloads/2025 ~/structure
16. mv -n ~/structure/2025 ~/structure/2024
17. mv -n ~/structure/2018/pictures/picture.png ~/structure/2018/pictures/Image.png   &&     mv -n ~/structure/2019/pictures/picture.png ~/structure/2019/pictures/Image.png   &&   
    mv -n ~/structure/2020/pictures/picture.png ~/structure/2020/pictures/Image.png   &&     mv -n ~/structure/2021/pictures/picture.png ~/structure/2021/pictures/Image.png   &&   
    mv -n ~/structure/2022/pictures/picture.png ~/structure/2022/pictures/Image.png   &&     mv -n ~/structure/2023/pictures/picture.png ~/structure/2023/pictures/Image.png   &&
    mv -n ~/structure/2024/pictures/picture.png ~/structure/2024/pictures/Image.png
18. mv -n ~/structure/2018/ ~/Documents/    &&        mv -n ~/structure/2024/ ~/Documents/    
19. rmdir -p ~/Documents/2024/
20. rm -r ~/Documents/2024/
21. cat > ~/structure/2019/files/data.md
22. nano ~/structure/2020/files/data.md
23. code ~/structure/2021/files/data.md
24. cat ~/structure/2020/files/data.md > ~/structure/2022/files/data.md
25. mkdir ~/structure/soft_links ~/structure/hard_links
26. ln -s ~/structure/2019/ ~/structure/soft_links/ && ln -s ~/structure/2020/ ~/structure/soft_links/ && ln -s ~/structure/2021/ ~/structure/soft_links/ && ln -s ~/structure/2022/ ~/structure/soft_links/ && ln -s ~/structure/2023/ ~/structure/soft_links/
27. ln -s ~/structure/2020/files/data.md ~/structure/hard_links/ && ln -s ~/structure/2021/.passwords/.passwords.txt ~/structure/hard_links/
28. mkdir structure/archives

30. mv ~/Downloads/image.jpg ~/structure/archives
31. tar -cvf structure/Image.tar structure/archives/image.jpg && tar -cvzf structure/Image.tar.gz structure/archives/image.jpg && tar -cvjf structure/Image.tar.bz2 structure/archives/image.jpg
32. zip -e -r structure.zip structure/ 