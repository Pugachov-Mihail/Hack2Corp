class GetUserBody {
  final String? mail;
  final String? password;

  GetUserBody({
    required this.mail,
    required this.password,
  });

  Map<String, dynamic> toApi() {
    return {
      'mail': mail,
      'password': password,
    };
  }
}