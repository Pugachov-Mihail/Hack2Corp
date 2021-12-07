class GetUserToken {
  final String? mail;
  final String? password;

  GetUserToken({
    required this.mail,
    required this.password,
  });

  Map<String, dynamic> toApi() {
    return {
      'username': mail,
      'password': password,
    };
  }
}