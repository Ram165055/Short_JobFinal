const tabs = document.querySelectorAll('[data-tab-target]')
const tabContents = document.querySelectorAll('[data-tab-content]')

tabs.forEach(tab => {
    tab.addEventListener('click',() => {
        const target = document.querySelector(tab.dataset.tabTarget)
        tabContents.forEach(tabcontent => {
            tabcontent.classList.remove('active')
        })
        tabs.forEach(tab => {
            tab.classList.remove('active')
        })
        tab.classList.add('active')
        target.classList.add('active')
    })
})

const tabsLG = document.querySelectorAll('[data-tab-targets]')
const tabContents1 = document.querySelectorAll('[data-tab-contents]')

tabsLG.forEach( tab =>{
  tab.addEventListener('click', () => {
    const targetLG = document.querySelector(tab.dataset.tabTargets)
    tabContents1.forEach(tabcontent => {
        tabcontent.classList.remove('active-line')
    })
    tabs.forEach(tab => {
        tab.classList.remove('active-line')
    })
    tab.classList.add('active-line')
    targetLG.classList.add('active-line')
    targetLG.classList.add('active-line')
  })
})
