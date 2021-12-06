import 'package:dio/dio.dart';
import 'package:shop_app/data/api/request/get_user_body.dart';
import 'package:shop_app/data/model/api_user.dart.dart';

class AutorizationService {
  static const _BASE_URL = '';

  final Dio _dio = Dio(
    BaseOptions(baseUrl: _BASE_URL),
  );

  Future<ApiUser> getUser(GetUserBody body) async {
    final response = await _dio.get(
      '/json',
      queryParameters: body.toApi(),
    );
    return ApiUser.fromApi(response.data);
  }
}