const mainController = ($scope) => {
     
  $scope.app = "Lista telefônica"
  
  $scope.classe = 'selecionado'

  $scope.list = [{
    name: 'Oscar',
    phone: '(000) 0000-0001'
  },{
    name: 'da',
    phone: '(000) 0000-0002'
  },{
    name: 'Silva',
    phone: '(000) 0000-0003'
  }]

  $scope.addContact = function(name, phone) {

    $scope.list.push({
      name: name,
      phone: phone
    })

    const input = $("input")

    input.map(index => {
      input[index].value = ''
    })

  }

}