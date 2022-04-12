# 疫情团购助手
当前上海是正处在防疫封控阶段，所有生活物资的采购基本靠各小区的志愿团长组织团购保供
商品，鉴于大家使用微信群接龙功能，导致团长最后的统计数据工作量比较大的情况，写一个
小插件帮助团长进行数据整理，也算是为抗疫尽自己的绵薄之力。

但是，本人实在是能力有限水平一般，目前完成的之后现在的这个样子，欢迎各位大佬们一起修改
小弟这里也谢过各位了。如果有什么问题，大家多交流。

## 使用说明
1. 首先对接龙格式的要求，每种商品开一次接龙，接龙格式为：
    
    楼栋门洞号 单元房间号 需要买的份数

   例如：
   ```commandline
   #接龙 老盛昌138套餐
   
   1. 16号 204室  1份
   2. 10号 404室  1份
   3. 12号 104室  1份
   4. 32号 504室  1份
   5. 20号 604室  1份
   6. 20号 602室  一份
   8. 12号 201室  1份
   9. 20号 402室  1份
   10. 3号甲 204室  1份
   11. 3号乙 206室  1份
   12. 20号 501室  2份
   ...诸如此类(程序采用了正则表达式进行了一定程度的容错，但依然建议团长们
   要求参团的人尽量使用规范格式，每个人用规范格式就可以大大提高整个流程的
   工作效率。：）
   ```
   
2. 接龙之后，在微信PC客户端将最终接龙的信息(如上例中)复制到一个文本文件下(.txt格式)，
并将该文本文件放在程序所在的目录下。
   1. 如果你有一定的代码基础，可以直接clone该项目，并在文件夹下运行
      ```bash
      python ./Gpurchase.py
      ```
      就会生成一个与txt文件同名的excel文件，打开该文件，提示错误是否修复，选择‘是’。
      就可以看到结果文件中存在两张工作表，‘整理好的数据’是已经规范好的数据，‘无法识别数据‘
      是程序无法识别的数据，如果这些数据仍有效需要整理，请团长们自己手动整理一下。
   2. 如果你不太熟悉代码，则请到release里下载我打包好的exe版本，并将其放在一个单独
      的文件夹内，并将你需要整理的文本文件也放在这个文件夹下，双击Gpurchase.exe文件
      完成后就可以看到与txt文件同名的excel结果文件了。打开该文件，提示错误是否修复，选择‘是’。
      就可以看到结果文件中存在两张工作表，‘整理好的数据’是已经规范好的数据，‘无法识别数据‘
      是程序无法识别的数据，如果这些数据仍有效需要整理，请团长们自己手动整理一下。

3. 感谢各位的使用，欢迎批评指正。