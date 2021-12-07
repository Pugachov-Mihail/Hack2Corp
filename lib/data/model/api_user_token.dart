class ApiUserToken {
  final String token;

  ApiUserToken.fromApi(Map<String, dynamic> map)
      : token = map['results']['token'];
}