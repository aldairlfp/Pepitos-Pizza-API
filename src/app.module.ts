import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { ClientModule } from './client/client.module';
import { BaseModule } from './base/base.module';
import { AddedModule } from './added/added.module';

@Module({
  imports: [ClientModule, BaseModule, AddedModule],
  controllers: [],
  providers: [],
})
export class AppModule {}
