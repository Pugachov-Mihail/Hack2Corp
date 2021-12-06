class ApiUser {
  final String name;
  final String surname;
  final String mail;
  final String password;

  ApiUser.fromApi(Map<String, dynamic> map)
      : name = map['results']['name'],
        surname = map['results']['surname'],
        mail = map['results']['mail'],
        password = map['results']['password'];
}