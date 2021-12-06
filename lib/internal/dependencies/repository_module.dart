import 'package:shop_app/data/repository/user_data_repository.dart';
import 'package:shop_app/domain/repository/user_repository.dart';

import 'api_module.dart';

class RepositoryModule {
  static UserRepository? _userRepository;

  static UserRepository? userRepository() {
    if (_userRepository == null) {
      _userRepository = UserDataRepository(
        ApiModule.apiUtil()!,
      );
    }
    return _userRepository;
  }
}