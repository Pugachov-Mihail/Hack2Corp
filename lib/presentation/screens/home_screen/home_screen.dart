import 'package:flutter/material.dart';

import 'components/body.dart';

class HomeScreen extends StatelessWidget {
  static String routeName = "/home_screen";
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Home screen"),
      ),
      body: Body(),
    );
  }
}
