   M S B A M L   `   `   `  ����I  EBMI_Calculator, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null/clr-namespace:BMI_CalculatorBMI_Calculator  5   	       BMI_Calculator.MainWindow   5   	   R NWindowsBase, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35\ XPresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35W SPresentationCore, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35D 9http://schemas.microsoft.com/winfx/2006/xaml/presentation    5   	   R NSystem.Xaml, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089:x,http://schemas.microsoft.com/winfx/2006/xaml     5   	   @d2http://schemas.microsoft.com/expression/blend/2008     5   	   Jmc;http://schemas.openxmlformats.org/markup-compatibility/2006     5   	   .localclr-namespace:BMI_Calculator     5   	     � Title$  
MainWindow��5   	   $	��700��6   $	��800��6)   .��5	      �  � ColumnDefinitions 5
   
   �� 5      $	��.5* �6   �� 5      $��1* �6   �� 5      $��1* �6   �� 5      $	��.5* �6   �� 5      $��1* �6   �� 5      $��1* �6   �� 5      $��1* �6   �� 5      $	��.5* �6    � RowDefinitions 5   
   �� 5      $	��.5* �6   �� 5      $��1* �6   �� 5      $��1* �6   �� 5      $��1* �6   �� 5      $��1* �6   �� 5      $��1* �6   �� 5      $��2* �6   �� 5      $��5* �6   �� 5      $	��.5* �6   .+�5!   
   �� $��
First Name��6   $��1��6%   $��1��62   �� 5"   
   $��
Last Name:��6   $��2��6%   $��1��62   �� 5#   
   $��Phone:��6   $��3��6!   $��1��6.   �� 5$   
   $��Height Inches:��6   $��4��6)   $��1��66   �� 5%   
   $��Weight Lbs:��6   $��5��6&   $��1��63   6E   �� 5&   
   $��	Your BMI:��6   $��24(�6$   $
��Bold"�62   $��1��6D   $��4��6Q   �� 5'   
   -   5         ��Name$ lblBmi��5'      $��0��6    $��32(�6,   $
��Bold"�6:   $��2��6L   $��4��6Y   �� 5)   
   -   5         ��Name$ xFirstNameBox��5)      $��1��6)   $��2��66   $��16(�6F   $��30��6T   �� 5*   
   -   5        $ xLastNameBox��5*      $��2��6(   $��2��65   $��16(�6E   $��30��6S   �� 5+   
   -   5        $ 	xPhoneBox��5+      $��3��6%   $��2��62   $��16(�6B   $��30��6P   �� 5,   
   -   5        $ xHeightInchesBox��5,      $��4��6,   $��2��69   $��16(�6I   $��30��6W   �� 5-   
   -   5        $ xWeightLbsBox��5-      $��5��6)   $��2��66   $��16(�6F   $��30��6T   �� 5/   
   $��BMI Results��6   $��50(�6&   $
��Bold"�64   $��3��6F   $��3��50      $��2��6$   $��4��65   �� 51   
   -   5        $ 
lblMessage��51      $��Message��6$   $��5��66   $��4��6C   $��20(�6S   $
��Bold"�6a   �� 53   
   -   5         ��Name$ 	SubmitBtn��53      $��Submit��6$   $��5��65   $��1��6B   $��2��6j   $��0,52,123,263q�6~   $��3��6�   �� 54   
   -	   5        $ ClearBtn��54      $��Clear��6#   $��6��63   $��3��6@   6P   �� 55   
   -
   5        $ 	ImportBtn��55      $��Import��6$   $��6��65   $��5��6B   �� 56   
   -   5        $ ExitBtn��56      $
��Exit��6"   $��6��61   $��7��6>   6N   &   System.Windows.Controls.DataGrid  58   
   -   5          Name$ 	xDataGrid��58         AutoGenerateColumns . $��1��6A   $
��Left=�59      $	��257��6.   $��7��6;   $	��Top=�5:      $	��722��6+   $��7��67   5;      5<      