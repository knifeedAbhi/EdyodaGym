import re   

class EdyodaGym:

    def __init__(self):
        
        self.cusInfo = list()   # info in form of [phone,name,sex,age,email,bmi,mem]
        self.regInfo = list()   #info in form of [phone,{regimen}]

    def regChart(self,index):
        self.index = index
        print('\n')
        if self.index<18.5:
            self.chart = {
                'Mon':'Chest',
                'Tue':'Biceps',
                'Wed':'Rest',
                'Thu':'Back',
                'Fri':'Triceps',
                'Sat':'Rest',
                'Sun':'Rest'
            }
            return self.chart

        elif self.index>=18.5 and self.index<25:
            self.chart = {
                'Mon': 'Chest',
                'Tue': 'Biceps',
                'Wed': 'Cardio/Abs',
                'Thu': 'Back',
                'Fri': 'Triceps',
                'Sat': 'Legs',
                'Sun': 'Rest'
            }
            return self.chart
            
        elif self.index>=25 and self.index<30:
            self.chart = {
                'Mon': 'Chest',
                'Tue': 'Biceps',
                'Wed': 'Cardio/Abs',
                'Thu': 'Back',
                'Fri': 'Triceps',
                'Sat': 'Legs',
                'Sun': 'Cardio'
            }
            return self.chart

        elif self.index>=30:
            self.chart = {
                'Mon': 'Chest',
                'Tue': 'Biceps',
                'Wed': 'Cardio',
                'Thu': 'Back',
                'Fri': 'Triceps',
                'Sat': 'Cardio',
                'Sun': 'Cardio'
            }
            return self.chart
            
    def show_admin_menu(self):
        
        print('\nYou have entered the administrative section.\n')
        print('1. Create a Member')
        print('2. View Member')
        print('3. Delete a member')
        print('4. Update a member')
        print('5. Create Regimen')
        print('6. View Regimen')
        print('7. Delete Regimen')
        print('8. Update Regimen')
        print('0. Exit')
        self.call = input('Enter the menu you want to visit: \n')
        if self.call=='1':
            self.createMember()
        elif self.call=='2':
            self.viewMember()
        elif self.call=='3':
            self.delMember()
        elif self.call =='4':
            self.updateMember()
        elif self.call =='5':
            self.regCreate()
        elif self.call =='6':
            self.regView()
        elif self.call =='7':
            self.regDel()
        elif self.call =='8':
            self.regUpdate()
        elif self.call =='0':
            print('\nLogging out as admin')
            pass
        else:
            print('Invalid Menu.\nPlease try again.')
            self.show_admin_menu()

    def createMember(self):
        print('Here you can create a member.')

        def custNoValidate():  # phone number validation
            cust_no = int(input('\nEnter your phone number: \n'))
            if self.cusInfo!=[]:
                for group in self.cusInfo:
                    for phone in group:
                        if cust_no==phone:
                            print('\nThis number is already registered.')
                            custNoValidate()
                        else:
                            continue
            try:
                if int(int(cust_no)/1000000000) > 0 and int(int(cust_no)/1000000000) < 10:
                    current_cust.append(cust_no)
                else:
                    print('\nPlease enter a valid phone number.\n')
                    custNoValidate()
            except ValueError:
                print('\nPlease enter a valid phone number.\n')
                custNoValidate()

        current_cust = list()

        def cusNameValidate():  # taking customer info and validating simultaneously
            cust_name = input('Enter the name: ')
            x = re.findall("[0-9]", cust_name)
            if len(x) != 0 or cust_name == '':
                print('\nInvalid character found in customer name.\n')
                cusNameValidate()
            else:
                current_cust.append(cust_name)

        def custGenValidate():  # gender validation
            cust_gend = input('\nEnter your gender (M/F/O): \n')
            cust_gend = cust_gend.upper()
            if cust_gend not in ['M', 'F', 'O']:
                print('\nEnter a valid gender.\n')
                custGenValidate()
            else:
                current_cust.append(cust_gend)

        def custAgeValidate():  # age validation
            try:
                cust_age = input('\nEnter your age: \n')
                if int(cust_age) < 1 or int(cust_age) > 110:
                    print('\nEnter a valid age.\n')
                    custAgeValidate()
                else:
                    current_cust.append(cust_age)
            except ValueError:
                print('\nPlease enter a valid age.\n')
                custAgeValidate()

        def custEmailValidate():  # email validation
            cust_email = input('\nEnter your email: \n')
            regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"

            if (re.search(regex, cust_email)):
                current_cust.append(cust_email)
            else:
                print('\nInvalid Email Address.\n')
                custEmailValidate()

        def custBmiValidate():  # bmi validation
            cust_bmi = int(input('\nEnter BMI:\n'))
            try:
                if cust_bmi < 1:
                    print('\nInvalid BMI.\n')
                    custBmiValidate()
                else:
                    current_cust.append(cust_bmi)
            except ValueError:
                print('\nPlease enter a valid BMI.\n')

        def membershipValidate():  # duration validation
            cust_mem = int(input('\nEnter duration of membership\n'))
            try:
                if cust_mem in [1, 3, 6, 12]:
                    current_cust.append(cust_mem)
                else:
                    print('\nTenure not availabe.\n')
                    membershipValidate()
            except ValueError:
                print('\Enter valid value.\n')
                membershipValidate()

        custNoValidate()
        cusNameValidate()

        custGenValidate()
        custAgeValidate()
        custEmailValidate()
        custBmiValidate()
        membershipValidate()

        self.cusInfo.append(current_cust)
        
        self.show_admin_menu()

    def viewMember(self):
        print('\nGet member info.')
        
        try:
            get_info = int(input('\nEnter the mobile number of the customer.\n'))
            iteration = 0
            if int(int(get_info)/1000000000) > 0 and int(int(get_info)/1000000000) < 10:
                for group in self.cusInfo:
                    
                    for phone in group:
                        
                        if get_info==phone:
                            
                            print('Name: ',group[1])
                            print('Age: ',group[3])
                            print('Sex: ',group[2])
                            print('Mob. No.: ',group[0])
                            print('Email: ',group[4])
                            print('BMI: ',group[5])
                            print('Membership Duration: ',group[6])
                            iteration=1
                self.show_admin_menu()

            elif iteration==0:
                print('\nNo records were found.')
                choice = input('\nDo you want to try again? (Y/N)')
                if choice.upper()=='Y':
                    self.viewMember()
                elif choice.upper()=='N':
                    self.show_admin_menu()
                else:
                    print('\nInvalid option.\nReverting to main menu.')
                    self.show_admin_menu()                
            else:
                print('\nPlease enter a valid phone number.\n')
                self.viewMember()
        except ValueError:
            print('\nPlease enter a valid phone number.\n')
            self.viewMember()

    def delMember(self):
        print('\nHere you can delete a member.\n')
        deleted = False
        choice = int(input('Enter the mobile number of the member whose record you want to delete:\n'))
        for group in self.cusInfo:
            for items in group:
                if choice == items:
                    self.cusInfo.remove(group)
                    print('\nRecord Successfully Deleted.\n')
                    deleted=True

        if deleted==False:
            again = input('\nSorry, no record found.\nDo you want to try again?(Y/N)\n')
            if again.lower()=='y':
                self.delMember()
            elif again.lower()=='n':
                self.show_admin_menu()
        else:
            self.show_admin_menu()

    def updateMember(self):
        print('\nHere you can update the records of members.\n')
        updatation = int(input('Enter the phone number of the record you want to update.\n'))
        for group in self.cusInfo:
            for items in group:
                if updatation==items:
                    print('Name: ', group[1])
                    print('Age: ', group[3])
                    print('Sex: ', group[2])
                    print('Mob. No.: ', group[0])
                    print('Email: ', group[4])
                    print('BMI: ', group[5])
                    print('Membership Duration: ', group[6])
                    print('Please choose from following option to update.')
                    print('1.Name\n2.Age\n3.Sex\n4.Mobile Number\n5.Email\n6.BMI\n7.Membership Duration\n')
                    choose = input()
                    if choose == '1':
                        def newName():
                            new_val = input('New Name:')
                            x = re.findall("[0-9]",new_val)
                            if len(x!=0) or len(new_val)==0:
                                print('\nInvalid Name')
                                newName()
                            else:
                                group[1]=new_val
                                print('\nRecord Successfully modified.')
                        newName()
                    elif choose=='2':
                        def newAge():
                            try:
                                new_val = n=int(input('New Age: '))
                                if new_val<1 or new_val>110:
                                    print('\nEnter valid age.')
                                    newAge()
                                else:
                                    group[3]=new_val
                                    print('\nRecord Successfully modified.')
                            except ValueError:
                                print('\nInvalid values')
                                newAge()
                                
                        newAge()
                    elif choose=='3':
                        def newGen():
                            new_val = input('New Sex:(M/F/O) ')
                            new_val= new_val.upper()
                            if new_val in ['M','F','O']:
                                group[2] = new_val
                                print('\nRecord Successfully modified.')
                            else:
                                print('\nInvalid Value.')
                                newGen()

                        newGen()
                    elif choose=='4':
                        def newNo():
                            try:
                                new_val = int(input('\nNew Mob. No.: '))
                                if int(int(new_val)/1000000000) > 0 and int(int(new_val)/1000000000) < 10:
                                    group[0] = new_val
                                    print('\nRecord Successfully modified.')
                                else:
                                    print('\nPlease enter a valid mobile number.')
                            except ValueError:
                                print('\nInvalid Mobile number entered.')
                                newNo()

                        newNo()
                    elif choose=='5':
                        def newMail():
                            new_val = input('\nNew Email: ')
                            regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
                            if (re.search(regex,new_val)):
                                group[4]= new_val
                                print('\nRecord Successfully modified.')
                            else:
                                print('\nInvalid Email.')
                                newMail()

                        newMail()
                    elif choose=='6':
                        def newBmi():
                            try:
                                new_val = int(input('\nNew BMI: '))
                                if new_val>=1:
                                    group[5]=new_val
                                    print('\nRecord Successfully modified.')
                                else:
                                    print('\nInvalid BMI')
                                    newBmi()
                            except ValueError:
                                print('\nInvalid BMI entered.')
                                newBmi()

                        newBmi() 
                        pass
                    elif choose=='7':
                        def newMem():
                            try:
                                new_val = int(input('New Membership Duration: '))
                                if new_val in [0,1,3,6,12]:
                                    group[6] = new_val
                                    print('\nRecord Successfully modified.')
                                else:
                                    print('\nInvalid Duration.')
                                    newMem()
                            except ValueError:
                                print('\nInvalid Duration.')
                                newMem()
                    else:
                        print('\nInvalid Option')
                        mem_choose = input('Do you wish to try again? (Y/N)')
                        if mem_choose.upper()=='Y':
                            newMem()
                        elif mem_choose.upper()=='N':
                            self.show_admin_menu()
                        else:
                            print('\nInvalid Option was chosen.\nReverting back to main menu.')
                            self.show_admin_menu()
        
        
        self.show_admin_menu()

    def regCreate(self):
        print('\nHere you can create for the members.')
        try:
            new_reg = int(input('\nEnter the mobile number of the member whose regimen you want to create.\n'))
            current_list = list()
            iteration = 0
            if int(int(new_reg)/1000000000) > 0 and int(int(new_reg)/1000000000) < 10:
                for group in self.cusInfo:
                    for items in group:
                        if new_reg==items:
                            regimen = self.regChart(group[5])
                            current_list.append(new_reg)
                            current_list.append(regimen)
                            
                            self.regInfo.append(current_list)
                            print('New Regimen is created successfully.')
                            iteration=1
                            
                            self.show_admin_menu()

                if iteration==0:
                    print('\nMember not found.')
                    choice = input('\nDo you want to try again? (Y/N)')
                    if choice.upper()=='Y':
                        self.regChart()
                    elif choice.upper()=='N':
                        self.show_admin_menu()
                    else:
                        print('\nInvalid option.\nReverting back to main menu.')
                        self.show_admin_menu()
            else:
                print('\nPlease enter valid number.')
                self.regCreate()

        except ValueError:
            print('\nInvalid number entered.')
            self.regCreate()
        pass

    def regView(self):
        print('\nHere you can view the regimen.')
        try:
            view = int(input('\nEnter the phone number of the member whose regimen you want to view.\n'))
            iteration = 0
            for group2 in self.regInfo:
                for phone in group2:
                    if view==phone:
                        display = group2[1]

                        for k,v in display.items():
                            print(k+' : '+v)
                        iteration=1
                        self.show_admin_menu()
            
            if iteration==0:
                print('\nRegimen not found for this number.')
                choice = input('\nDo you want to try again? (Y/N) ')
                if choice.upper()=='Y':
                    self.regView()
                elif choice.upper()=='N':
                    self.show_admin_menu()
                else:
                    print('\nInvalid option.\nReverting to main menu.')
                    self.show_admin_menu()
        except ValueError:
            print('\nInvalid number is entered.')
            self.regView()
                    
    def regDel(self):
        print('\nHere regimen can be deleted.')
        try:
            delete = int(input('\nEnter the mobile number of the member whose record is to be deleted.\n'))
            iteration = 0
            for group2 in self.regInfo:
                for phone in group2:
                    if delete==phone:
                        self.regInfo.remove(group2)
                        print('\nRegimen deleted successfully.')
                        iteration=1
                        self.show_admin_menu()
            if iteration==0:
                print('\nRegimen not found for this number.')
                choice = input('\nDo you want to try again? (Y/N) ')
                if choice.upper() == 'Y':
                    self.regDel()
                elif choice.upper() == 'N':
                    self.show_admin_menu()
                else:
                    print('\nInvalid option.\nReverting to main menu.')
                    self.show_admin_menu()
            
        except ValueError:
            print('\nInvalid number is entered.')
            self.regDel()

    def regUpdate(self):
        print('\nHere you can update the regimen of the member.')
        try:
            updating = int(input('\nEnter the phone number of the member whose regimen you want to update.\n'))
            iteration = 0
            for group2 in self.regInfo:
                for phone in group2:
                    if updating==phone:
                        for k,v in group2[1].items():
                            print(k,':',v)
                        
                        
                        def updates():
                            print('\nPlease choose the day you want to update.')
                            print('\n1.Mon\n2.Tue\n3.Wed\n4.Thu\n5.Fri\n6.Sat\n7.Sun')
                            choose = input()
                            if choose == 'Mon':
                                group2[1][choose] = input('\nPlan for Monday\n')
                                print('\nRegimen updated successfully.')
                                iteration=1
                            elif choose == 'Tue':
                                group2[1][choose] = input('\nPlan for Tuesday\n')
                                print('\nRegimen updated successfully.')
                                iteration = 1
                            elif choose == 'Wed':
                                group2[1][choose] = input('\nPlan for Wednesday\n')
                                print('\nRegimen updated successfully.')
                                iteration = 1
                            elif choose == 'Thu':
                                group2[1][choose] = input('\nPlan for Thursday.\n')
                                print('\nRegimen updated successfully.')
                                iteration=1
                            elif choose == 'Fri':
                                group2[1][choose] = input('\nPlan for Friday.\n')
                                print('\nRegimen updated successfully.')
                                iteration=1
                            elif choose == 'Sat':
                                group2[1][choose] = input('\nPlan for Saturday.\n')
                                print('\nRegimen updated successfully.')
                                iteration=1
                            elif choose == 'Sun':
                                group2[1][choose] = input('\Plan for Sunday.\n')
                                print('\nRegimen updated successfully.')
                                iteration=1
                            else:
                                print('\nInvalid Option.')
                                choose2 = input('\nDo you wan to try again? (Y/N)')
                                if choose2.upper() == 'Y':
                                    updates()
                                elif choose2.upper() == 'N':
                                    self.show_admin_menu()
                                else:
                                    print('\nInvalid option.\nReverting to main menu.')
                                    self.show_admin_menu()
                        updates()
                        self.show_admin_menu()
            if iteration==0:
                print('\nRegimen for this member was not found.')
                choice = input('\nDo you want to try again? (Y/N) ')
                if choice.upper() == 'Y':
                    self.regUpdate()
                elif choice.upper() == 'N':
                    self.show_admin_menu()
                else:
                    print('\nInvalid option.\nReverting to main menu.')
                    self.show_admin_menu()
        except ValueError:
            print('\nInvalid number is entered.')
            self.regUpdate()

    def mem_profile(self):
        for group in self.cusInfo:
            for phone in group:
                if self.username==phone:
                    print('Name: ',group[1])
                    print('Age: ',group[3])
                    print('Sex: ',group[2])
                    print('Mob. No.: ',group[0])
                    print('Email: ',group[4])
                    print('BMI: ',group[5])
                    print('Membership Duration: ',group[6])
        self.mem_menu(self.username, self.password)

    def mem_regimen(self):
        for group2 in self.regInfo:
            for phone in group2:
                if self.username==phone:
                    display = group2[1]
                    for k,v in display.items():
                        print(k+' : '+v)
        else:
            print('\nYour regimen has not been created by admin.\nContact admin for more details\n')
        self.mem_menu(self.username,self.password)

    def mem_menu(self,username,password):
        self.username = username
        self.password = password
        iteration=0
        for group in self.cusInfo:
            for phone in group:
                if self.username==phone:
                    if self.password==group[1]:
                        print("\nYou have entered the Member's lounge.\nHere you can take a look at your profile as well as your regimen.")
                        print('\n1. Check your profile')
                        print('\n2. Check your regimen')
                        print('\n0. Exit')
                        try:
                            self.call = int(input('\nChoose the required menu.\n'))
                            iteration=1
                            if self.call == 1:
                                self.mem_profile()  #test
                            elif self.call == 2:
                                self.mem_regimen()
                            elif self.call== 0:
                                print('\nLogging out as member.')
                            else:
                                print('\nInvalid option.\nTry again.')
                        except ValueError:
                            print('\nInvalid value.')
                            self.mem_menu(self.username,self.password)
        if iteration==1:
            pass
        else:
            print('\nNo members have been added yet.\nThis menu will be available only when admin will create some members.')

def start():
    print('Welcome to Edyoda Gym')
    obj = EdyodaGym()  # obj creation
    print('\nEnter your user type.\n')
    types = input('Admin/Member (A/M): ')
    
    def admin_Login():
        username = input('Username: ')  #default = admin
        password = input('Password: ')  #default = admin
        
        if username=='admin' and password=='admin':
            
            obj.show_admin_menu()                                                   #menu shown
        else:
            print('\nInvalid username and password.\n')
            choice = input('\nDo you wish to try again? (Y/N)')
            if choice.lower()=='y':
                admin_Login()
            elif choice.lower()=='n':
                start()
            else:
                print("\nInvalid option.\nLet's start again.\n")
                start()

    def member_login():
        username = int(input('\nEnter your phone number: \n'))
        password = input('\nEnter your name as password.\n')
        try:
            if int(int(username)/1000000000) > 0 and int(int(username)/1000000000) < 10:
                x = re.findall("[0-9]", password)
                if len(x)!=0 or password=='':
                    print('\nInvalid username or password.\n')
                    choice = input('\nDo you want to try again? (Y/N)\n')
                    if choice.upper() == 'Y':
                        member_login()
                    elif choice.upper()=='N':
                        start()
                    else:
                        print('\nInvalid option.\Reverting back to login page.\n')
                        start()
                
                else:
                    obj.mem_menu(username,password)                                      #menu shown
            else:
                print('\nPlease enter correct values.')

        except ValueError:
            print('\nInvalid option.\nReverting back to login page.\n')
            start()

    def start_option(types):
        if types.lower() =='a':
            admin_Login()
        elif types.lower() =='m':
            member_login()
        else:
            print('\nWrong input.')
        
        choice = input('\nDo you wish to login again? (Y/N)\n')
        if choice.upper()=='Y':
            types = input('Admin/Member (A/M): ')
            start_option(types)
        elif choice.upper()=='N':
            print('\nThank you for working with Edyoda Gym.\nSee you soon.')
        else:
            print('\nInvalid option.\nExiting the application.\n\nThank you for working with Edyoda Gym.\nSee you soon.')

    start_option(types)

start()


