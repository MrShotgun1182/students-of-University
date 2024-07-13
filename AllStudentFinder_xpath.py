XPATH = {
    'main_page' : {
        'samaneMorvarid' : '/html/body/div[2]/div/section[2]/div/div[2]/div[2]/div/div[1]/a[1]'
    },
    'dashbord' :{
        'vorodBeSamane' : '//*[@id="agLoad"]/div/div/app-root/app-profile-public/div/app-public/mat-sidenav-container/mat-sidenav-content/div/div/div[2]/mat-list[1]/div/mat-grid-list/div/mat-grid-tile[1]/div/div/a'
    },
    'login_page' : {
        'username' : 'mat-input-0',
        'password' : "mat-input-1",
        'vorod' : "/html/body/div[1]/div/div/app-root/app-singin/div/app-singin-user/div/div/div[2]/form/div[1]/div[2]/div/mat-card-content/div/mat-card-actions/div/button"   
    },
    'user_panel' :{
        'tabligh' : "/html/body/div[1]/div/div/app-root/app-main/div/app-dashboard/mat-sidenav-container/mat-sidenav-content/div/div[1]/div/mat-tab-group/mat-tab-header/div/div/div/div[2]/div/div/div[3]/mat-icon",
        'socialNetworkbuttom' : '/html/body/div[1]/div/div/app-root/app-main/div/app-dashboard/mat-sidenav-container/mat-sidenav-content/div/div[1]/div/div[2]/button[1]/span[1]/mat-icon',
    },
    'socialNetwork' :{
        'socialNetworkframe' : '/html/body/div[1]/div/div/app-root/app-main/div/app-dashboard/mat-sidenav-container/mat-sidenav[2]/div/mat-nav-list/div/app-left-menu/iframe',
        'students_group' : '/html/body/div[1]/div/div/app-root/app-chat/div/app-contact/div/div/div/div[10]',
        'hamburger_list' : '/html/body/div[1]/div/div/app-root/app-chat/div/app-message/div/header/div[2]/div[2]/button[2]/span[1]/mat-icon',
        'group_management' : '/html/body/div[4]/div[2]/div/div/div/div[1]/div/div/button',
        'scrollElement' : '//*[@id="scroll"]',
    }
}

def get_XPATH (part , element):

    return XPATH[part][element]


