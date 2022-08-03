import { Test, TestingModule } from '@nestjs/testing';
import { AddedService } from './added.service';

describe('AddedService', () => {
  let service: AddedService;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      providers: [AddedService],
    }).compile();

    service = module.get<AddedService>(AddedService);
  });

  it('should be defined', () => {
    expect(service).toBeDefined();
  });
});
